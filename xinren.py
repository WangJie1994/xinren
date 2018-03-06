# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:03:11 2018

@author: wangj
"""

import numpy as np
import pandas as pd

#读取数据集
path = 'C:/Users/wangj/Documents/tianchi/xinren/fresh_comp_offline'

tianchi_fresh_comp_train_item = pd.read_csv(path + '/tianchi_fresh_comp_train_item.csv')
tianchi_fresh_comp_train_user = pd.read_csv(path + '/tianchi_fresh_comp_train_user.csv')

#查看数据
tianchi_fresh_comp_train_item.head(5)
tianchi_fresh_comp_train_user.head(5)

tianchi_fresh_comp_train_user['time'].value_counts()
tianchi_fresh_comp_train_user['behavior_type'].value_counts()

#筛选出加入购物车的数据
train_user = tianchi_fresh_comp_train_user[tianchi_fresh_comp_train_user['behavior_type']==3]

#筛选出12月18号一天的数据
import re
regex = re.compile(r'^2014-12-18+ \d+$')

def date(column):
    if re.match(regex, column['time']):
        date, hour = column['time'].split(' ')
        return date
    else:
        return 'null'

train_user['time'] = train_user.apply(date, axis=1)

train_user=train_user[(train_user['time'] =='2014-12-18')]

# 删除掉多余项
train_user=train_user.drop(['user_geohash'],axis=1)
train_user=train_user.drop(['item_category'],axis=1)
train_user=train_user.drop(['behavior_type'],axis=1)
train_user=train_user.drop(['time'],axis=1)

train_user['item_id'].count()

train_user.to_csv(path+ '/myPredict.csv',index=False)
