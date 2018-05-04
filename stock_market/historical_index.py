# -*- coding=utf-8 -*-

"""
Purpose:
    Use Tushare to get historical re-balanced prices for Shanghai and Shenzhen index.

Author:
    Yuhao Zhu

Version:
    20170405: Download historical index.
"""

import tushare as ts
import pandas as pd

index_list = ['sh', 'sz', 'hs300', 'sz50', 'zxb', 'cyb']
df_prices = ts.get_k_data("sh", start='2011-01-01', end='2017-02-28')
#df_prices['name_index'] = index_list[0]
print('Get historical prices for index {}'.format(index_list[0]))
all_number = len(index_list)
print('{} index out of {} downloaded.'.format(1, all_number))
print('The data set has {} rows.\n'.format(len(df_prices.index)))

print(df_prices)

count = 2
for index in index_list[1:]:
    df_index = ts.get_k_data(index, start='2011-01-01', end='2017-02-28')
#    df_index['name_index'] = index
    print('Get historical prices for index {}.'.format(index))
    df_prices = pd.concat([df_prices, df_index])
    print('{} index out of {} downloaded.'.format(count, all_number))
    print('The data set has {} rows.\n'.format(len(df_prices.index)))
    count += 1

print(df_prices)

df_prices.to_csv('data/index_20110101_20170228.csv', encoding='utf-8-sig')