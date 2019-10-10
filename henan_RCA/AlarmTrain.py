import pandas as pd
import time
import numpy as np
import pickle
import os
import sys
import re
import warnings
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
warnings.filterwarnings('ignore')           #不显示警告
print("导入包完成！")

#%%
#1、读取数据
Dir = '/root/AI告警分析数据/告警'
File = os.path.join(Dir, 'alarm_20190914.csv')
df = pd.read_csv(File, sep='^')
print("完成数据加载！")
print("原始数据维度", df.shape)

#2、过滤4级告警
df = df[df['网管告警级别']!=4].copy()
df.reset_index(drop=True, inplace=True)
print("滤除4级告警后的数据维度为",df.shape)

#3、过滤衍生告警 和未匹配告警
df = df[df['告警标题'].apply(lambda x:np.nan if '衍生' in str(x) else x).notnull()].copy()
df = df[df['告警标题']!='未匹配告警'].copy()
print("滤除衍生告警后的数据维度为",df.shape)

#加载补充信息表
vendor_ring = pd.read_csv('/root/AI告警分析数据/ring_vendor_id_name.csv',sep='\t')
vendor_ring.rename(columns={'device_id':'厂家ID'}, inplace=True)
vendor_ring.drop_duplicates('厂家ID', inplace=True)
vendor_ring['厂家ID'] = vendor_ring['厂家ID'].apply(lambda x:np.nan if '-' in x else int(x))
#
vendor_nring = pd.read_csv('/root/AI告警分析数据/notring_vendoer_id_name.csv',sep='\t')
vendor_nring.rename(columns={'device_id':'厂家ID'}, inplace=True)
vendor_nring.drop_duplicates('厂家ID', inplace=True)
#
device_id_name = pd.read_csv('/root/AI告警分析数据/device_id_type.csv',sep='\t')
#
version = pd.read_csv('/root/codes/RCA/alarm_norm_file/version.csv')
version.rename(columns={'网管告警ID':'alarmid_sup'}, inplace=True)
version.dropna(subset=['厂家'], inplace=True)
version.drop_duplicates(subset=['厂家', '厂家告警ID'], inplace=True)

print("网管告警ID缺失数据条数",df['网管告警ID'].isnull().sum())
#拼接设备类型名称
data = df.merge(device_id_name, on=['设备类型ID'], how='left')
print(data.shape)
#切分动环和非动环数据
df_nr = data[data['专业ID']!=8].copy()
df_r = data[data['专业ID']==8].copy()

#拼接厂家设备名
df_nr = df_nr.merge(vendor_nring, on=['厂家ID'], how='left')
df_r = df_r.merge(vendor_ring, on=['厂家ID'], how='left')
data = pd.concat([df_nr, df_r], axis=0)
data.rename(columns={'device_name':'厂家'}, inplace=True)
data['厂家'] = data['厂家'].apply(lambda x:'摩托罗拉' if '摩托罗拉' in str(x) else x)
print(data.shape)

#拼接厂家告警ID,只填充少数网管告警ID
data  = data.merge(version[['厂家', '厂家告警ID', 'alarmid_sup']], on=['厂家', '厂家告警ID'], how='left')
data.loc[data['网管告警ID'].isnull(), '网管告警ID'] = data[data['网管告警ID'].isnull()]['alarmid_sup']
print("网管告警ID仍然缺失数据条数",data['网管告警ID'].isnull().sum())


#%%开始训练
#5、转换标准时间为时间戳，用于密度聚类
data['timestamp'] = pd.to_datetime(data['发生时间'])
data['timestamp'] = pd.to_timedelta(data.timestamp).dt.total_seconds()
data.sort_values(by=['timestamp'], inplace=True)

train = data[['专业ID', '告警标题', '厂家告警级别',  '网元名称', '厂家', '设备类型名称', '地市ID', 'timestamp']]
train.columns = ['specialtyid', 'alarm_title', 'alarm_level', 'deveice_name', 'vendor', 'device_type_name', 'city', 'timestamp']

specialty_dict = {1:'无线',2:'核心网',6:'传输',8:'动环'}
train['specialty'] = train['specialtyid'].map(specialty_dict)
train.groupby(['specialty']).size()

#pair_id
train['pair_id'] = train['alarm_title'] + '_' + train['deveice_name']

train.groupby('city').size()
train = train.query('city!=0').query('city!=2014').copy()

###用于提交多个进程任务
cities = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
city = cities[int(sys.argv[1])]
train = train[train['city']==city].copy()

info_table = train.drop_duplicates(subset=['pair_id'], keep='first')
city_eps_ms = {
 2000:(5,1),
 2001:(11,1),
 2002:(6,1),
 2003:(11,1),
 2004:(7,1),
 2005:(5,1),
 2006:(14,1),
 2007:(11,1),
 2008:(5,1),
 2009:(11,1),
 2010:(11,1),
 2011:(3,1),
 2012:(10,1),
 2013:(8,1)
}
eps, ms = city_eps_ms[city]

#6、采用DBSCAN聚类划分时域
features = train[['timestamp']].values
clustering = DBSCAN(eps=eps, min_samples=ms).fit(features)#labal=226
labels = clustering.labels_
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
print('Estimated number of clusters: %d' % num_clusters)
print('Estimated number of noise points: %d' % n_noise)
print("完成聚类！")

#聚类后的时间片划分结果
train['label'] = labels

#滤除异常点
train = train[train['label'] != -1]
train.reset_index(drop=True, inplace=True)
print("训练数据维度", train.shape)


###开始关联分析挖掘频繁二元项集
st = time.time()
support = 15
itemsets = []
SupL1, TotalList = {}, []
lift, conf = 1, 0.7
for k, group in train.groupby('label'):
    TotalList.extend(list(group['pair_id'].values))
    items = frozenset(group['pair_id'].values)
    itemsets.append(items)
    for item in items:
        SupL1[item] = SupL1.get(item, 0)
        SupL1[item]+=1
SupL1 = {item:freq for item, freq in SupL1.items() if freq>=support}
print('频繁项数', len(SupL1))

ds_dict = dict(zip(itemsets, range(len(itemsets))))

#生成Eclat算法的输入
ec_data = {}
for trans, idxmap in ds_dict.items():
    for item in SupL1:
        if item in trans:
            if item in ec_data:
                ec_data[item].append(idxmap)
            else:
                ec_data[item] = [idxmap]

#计算二元频繁项
patterns = {}
for item1 in SupL1:
    for item2 in  SupL1.keys():
        freq = len(set(ec_data[item1])&set(ec_data[item2]))
        if freq>=support:
             patterns.update({(item1,item2):freq})

print("二元项集数目", len(patterns))
ana_time = time.time()-st
print("完成关联分析所花时间 %.3f!" %ana_time)


#开始对二元项集进行关联分析生成主次告警对
pair_rules = {}
for pair, freq in patterns.items():
    if len(pair) == 2:
        cond_prob = freq / min(SupL1[pair[0]], SupL1[pair[1]])
        if SupL1[pair[0]] > SupL1[pair[1]]:
            pair = (pair[1], pair[0])
        else:
            pair = (pair[0], pair[1])
        lift_prob = len(itemsets) * freq / (SupL1[pair[0]]*SupL1[pair[1]])
        if lift_prob >= lift and cond_prob >= conf:
            pair_rules[pair] = freq
###
info_cols = ['alarm_title', 'alarm_level', 'deveice_name', 'device_type_name', 'vendor', 'specialtyid']
rule_cols = ['master_title', 'master_level', 'master_device_name', 'master_device_type', 'master_vendor','master_specialty',
             'slave_title', 'slave_level', 'slave_device_name', 'slave_device_type', 'slave_vendor','slave_specialty',
             'support', 'master_freq', 'slave_freq', 'total_itemsets', 'confidence', 'lift']

rule = []
total_itemsets = int(len(itemsets))

for (master, slave), freq in pair_rules.items():
    tmp = info_table[info_table['pair_id']==master][info_cols].values.tolist()[0]
    tmp.extend(info_table[info_table['pair_id']==slave][info_cols].values.tolist()[0])
    tmp.extend([freq, int(SupL1[master]),
             int(SupL1[slave]),
             total_itemsets,
             freq/int(SupL1[master]),
             freq*len(itemsets)/int(SupL1[master])/int(SupL1[slave])])
    rule.append(tmp)

rule = pd.DataFrame(rule, columns=rule_cols)
ana_time = time.time()-st
print("完成关联挖掘所花时间%.3f！"%ana_time)


st = time.time()
#保留主告警等级<=次告警等级，去除存在衍生告警的告警
rule = rule[rule.master_level<=rule.slave_level].copy()
rule['wrong_flag'] = rule.master_title.apply(lambda x:1 if '衍生' in x else 0)
#主次告警的标题和网元类型若相同，black_flag=1 否则black_flag=0
rule['black_flag'] = 0
rule.loc[(rule.master_title==rule.slave_title)&(rule.master_device_name==rule.slave_device_name), 'black_flag'] = 1
#拓扑关系校验，存在拓扑关系，topo_flag;否则topo_flag=0
# def TopoTest(x):
#       return int(x[0]==x[1] or (x[0] in G) and (x[1] in G) and (nx.has_path(G, x[0], x[1])))
# rule['topo_flag'] = rule[['master_device_id', 'slave_device_id']].apply(TopoTest, axis=1)
#保留拓扑与有效规则
rule = rule.query('black_flag==0').query('wrong_flag==0').copy()
#去除flag字段
rule.drop(['black_flag'], axis=1, inplace=True)


rule['same_flag'] = 0
rule.loc[rule.master_device_name==rule.slave_device_name, 'same_flag'] = 1
#将主次告警表存到本地路径下
rule.to_csv('RawRules/MSID_Rules_%d.csv'%city, sep=',', index=None)

print("完成规则筛选所花时间 %3.f" %(time.time()-st))

with open('record.txt', 'a') as f:
    f.write("city:%d, eps:%d, min_samples:%d, 团簇数:%d,  二元项集数目:%d,关联分析时间:%.3f, 关联挖掘所花时间:%.3f \n"
            %(city, eps, ms, num_clusters,  len(patterns), ana_time, time.time()-st))