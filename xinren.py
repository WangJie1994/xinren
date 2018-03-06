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

tianchi_fresh_comp_train_item.head(5)
tianchi_fresh_comp_train_user.head(5)