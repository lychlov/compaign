# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:39:07 2019

@author: Administrator
"""

import pandas as pd
import os
import sys

#%%对上一步AlarmTrain生成的粗糙进行规则泛化

Files = os.listdir('RawRules')

df = [pd.read_csv(os.path.join('RawRules', File)) for File in Files if 'MSID' in File]
rule = pd.concat(df, axis=0)

gpcols = ['same_flag', 'master_title', 'master_vendor', 'master_device_type','master_specialty',
          'slave_title', 'slave_vendor', 'slave_device_type', 'slave_specialty']
aggfunc = {'support':'sum', 'master_freq':'sum', 'slave_freq':'sum','total_itemsets':'sum'}
aggthis = rule.groupby(gpcols).agg(aggfunc)
aggthis['conf'] = aggthis['support'] / aggthis['master_freq']
aggthis['lift'] = aggthis['support'] * aggthis['total_itemsets'] / ( aggthis['master_freq'] *  aggthis['slave_freq'])
#对于主次告警提升度大于0.7的规则进行保留
aggthis = aggthis[aggthis['lift']>0.7].copy()
aggthis.reset_index(inplace=True)
aggthis.to_csv('MSNe_Rules.csv', index=None, sep=',')
print("完成输出网元类型表！")