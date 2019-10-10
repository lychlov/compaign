import pandas as pd
import numpy as np
import os
import sys
import re
import warnings
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import time
sys.setrecursionlimit(100000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
warnings.filterwarnings('ignore')           #不显示警告
print("导入包完成！")
st = time.time()


#1、读取数据
Dir = '/root/AI告警分析数据/告警'
File = os.path.join(Dir, 'alarm_20190914.csv')
df = pd.read_csv(File, sep='^')
print("完成数据加载！")
print("原始数据维度", df.shape)


#3、去除4级告警对算法模型的干扰
df = df[df['网管告警级别']!=4].copy()
df.reset_index(drop=True, inplace=True)
print("滤除4级告警后的数据维度为",df.shape)


#4、加载补充信息表，如厂家ID与厂家名的映射关系，厂家名与厂家告警ID的映射关系，网元名称与网元ID的映射关系

#厂家ID与厂家名的映射关系
vendor_ring = pd.read_csv('/root/AI告警分析数据/ring_vendor_id_name.csv',sep='\t')
vendor_ring.rename(columns={'device_id':'厂家ID'}, inplace=True)
vendor_ring.drop_duplicates('厂家ID', inplace=True)
vendor_ring['厂家ID'] = vendor_ring['厂家ID'].apply(lambda x:np.nan if '-' in x else int(x))

#厂家ID与厂家名的映射关系
vendor_nring = pd.read_csv('/root/AI告警分析数据/notring_vendoer_id_name.csv',sep='\t')
vendor_nring.rename(columns={'device_id':'厂家ID'}, inplace=True)
vendor_nring.drop_duplicates('厂家ID', inplace=True)

#网元名称与网元ID的映射关系
device_id_name = pd.read_csv('/root/AI告警分析数据/device_id_type.csv',sep='\t')

#厂家名与厂家告警ID的映射关系
version = pd.read_csv('/root/codes/RCA/alarm_norm_file/version.csv')
version.rename(columns={'网管告警ID':'alarmid_sup'}, inplace=True)
version.dropna(subset=['厂家'], inplace=True)
version.drop_duplicates(subset=['厂家', '厂家告警ID'], inplace=True)


#5、拼接设备类型名称
print("网管告警ID缺失数据条数",df['网管告警ID'].isnull().sum())
data = df.merge(device_id_name, on=['设备类型ID'], how='left')

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


#6、转换标准时间为时间戳，用于密度聚类
data['timestamp'] = pd.to_datetime(data['发生时间'])
data['timestamp'] = pd.to_timedelta(data.timestamp).dt.total_seconds()
data.sort_values(by=['timestamp'], inplace=True)


#7、逐地市对告警信息进行根因分析，首先对不同地市采取聚类，基本划分为5-10分钟为一段周期，根据先前模型训练得到的规则表，对其进行告警压缩
RemoveSlave = []
#参数集
city_eps_ms = {
 2000:(5,1), 2001:(11,1), 2002:(6,1), 2003:(11,1), 2004:(7,1), 2005:(5,1), 2006:(14,1),
 2007:(11,1), 2008:(5,1), 2009:(11,1), 2010:(11,1), 2011:(3,1), 2012:(10,1), 2013:(8,1)
}

for city, (eps, ms) in city_eps_ms.items():
    #7.1、采用DBSCAN聚类划分时域
    train = data.query('地市ID==%d'%city).copy()
    features = train[['timestamp']].values
    clustering = DBSCAN(eps=eps, min_samples=ms).fit(features)#labal=251
    labels = clustering.labels_
    num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    print('Estimated number of clusters: %d' % num_clusters)
    print('Estimated number of noise points: %d' % n_noise)
    print("完成聚类！")
    train['label'] = labels

    #7.2、滤除异常点
    train = train[train['label'] != -1]
    train.reset_index(drop=True, inplace=True)
    print("训练数据维度", train.shape)
    #选取与规则字段对应的数据，用于后续分析
    cols1 = ['专业ID', '告警标题', '网管告警级别',  '网元名称', '厂家', '设备类型名称', '地市ID', 'timestamp', '网管告警ID',
              '是否与对端网元相关', '该事件对业务的影响','label','发生时间','清除时间']
    cols2 = ['specialtyid', 'alarm_title', 'alarm_level', 'deveice_name', 'vendor', 'device_type_name', 'city', 'timestamp',
                     'alarm_id', 'isvendorcor', 'isinfluence', 'label','starttime','cleartiem']
    rename_map = dict(zip(cols1, cols2))
    train = train.rename(columns=rename_map)

    specialty_dict = {1:'无线',2:'核心网',6:'传输',8:'动环'}
    train['specialty'] = train['specialtyid'].map(specialty_dict)
    train.groupby(['specialty']).size()

    #pair_id
    train['pair_id'] = train['alarm_title'] + '_' + train['deveice_name']

    #7.3、读取湖南数据生成的规则表，进行告警压缩
    # HisRules = pd.read_csv('MSNe_Rules.csv')
    HisRules = pd.read_csv('/root/AI告警分析数据/batch/MSNe_Rules.csv')
    MasterId = set(HisRules['master_title'].values)
    SlaveId = set(HisRules['slave_title'].values)
    MasterSlaveAlarm = dict(HisRules.groupby('slave_title').agg({'master_title':'unique'}).reset_index().values)
    MasterSlaveAlarm = {key:set(values) for key, values in MasterSlaveAlarm.items()}

    for idx, group in train.groupby('label'):
        MasterTmp = set(group['alarm_title'].values)&MasterId
        SlaveTmp = set(group['alarm_title'].values)&SlaveId
        if MasterTmp and SlaveTmp:
            for slave_id in SlaveTmp:
                if len(MasterTmp&MasterSlaveAlarm[slave_id])>=1:
                    RemoveSlave.append(slave_id)



#8、输出告警压缩和去重的数据
RemoveSlavedf = pd.DataFrame(list(set(RemoveSlave)), columns=['告警标题'])
RemoveSlavedf['IsRemove'] = 1
RM_data = data.merge(RemoveSlavedf, on='告警标题', how='left')
RM_data = RM_data.query('IsRemove!=1').copy()
print('压缩后数据维度',RM_data.shape)
RM_data.drop_duplicates(['告警标题','网元名称'], inplace=True)
print('去重后后数据维度',RM_data.shape)
print("完成第一轮的告警压缩！")
print("压缩率为：", 1-RM_data.shape[0]/data.shape[0])



#9、去除三级告警
print("去除三级告警后数据维度",RM_data[RM_data['网管告警级别']!=3].shape)
RM_data = RM_data[RM_data['网管告警级别']!=3].copy()


#10、去除发生时间与清楚时间相隔一分钟内的数据
RM_data['starttime'] = pd.to_datetime(RM_data['发生时间'])
RM_data['starttime'] = pd.to_timedelta(RM_data.starttime).dt.total_seconds()
RM_data.sort_values(by=['starttime'], inplace=True)

RM_data['endtime'] = pd.to_datetime(RM_data['清除时间'])
RM_data['endtime'] = pd.to_timedelta(RM_data.endtime).dt.total_seconds()
RM_data.sort_values(by=['endtime'], inplace=True)

RM_data['delttime'] = RM_data['endtime'] - RM_data['starttime']

print("告警发生与清除时间差大于1分钟的数据维度", RM_data[RM_data['delttime']>60].shape)
RM_data = RM_data[RM_data['delttime']>60].copy()


#11、去除去除编码非标准化的告警数据
print("去除编码非标准化的告警信息", RM_data['网管告警ID'].notnull().sum())
RM_data = RM_data[RM_data['网管告警ID'].notnull()].copy()


print("完成告警压缩总时间", (time.time()-st)/60)