# -*- coding=utf-8 -*-

"""
Purpose:
    Use Tushare to get historical re-balanced prices for listed Chinese firms on Shanghai and Shenzhen markets.

Author:
    Yuhao Zhu

Version:
    20170313: Download historical stock prices.
"""

import tushare as ts
import pandas as pd
# df_basics = ts.get_stock_basics()
# df_basics.to_csv('data/stock_basics.csv', encoding='utf-8-sig')
# stock_list = df_basics.index.get_values()
# print('Get stock list!')

df_basics = pd.read_csv('data/stock_basics.csv', encoding='utf-8-sig')
stock_list = df_basics.code
stock_list_str = []
for stock in stock_list:
    stock = '{0:06d}'.format(stock)
    stock_list_str.append(stock)
stock_list = stock_list_str

with open('data/stock_list.txt', 'w', encoding='utf-8-sig') as writer:
    for stock in stock_list:
        writer.write('{}\n'.format(stock))
    writer.close()

df_prices = ts.get_k_data(stock_list[0], start='2012-12-01', end='2017-02-28')
df_prices['code'] = stock_list[0]
print('Get historical prices for stock {}'.format(stock_list[0]))
all_number = len(stock_list)
print('{} stocks out of {} downloaded.'.format(1, all_number))

count = 2
for stock in stock_list[1:]:
    df_stock = ts.get_k_data(stock, start='2011-01-01', end='2017-02-28')
    df_stock['code'] = stock
    print('Get historical prices for stock {}.'.format(stock))
    df_prices = pd.concat([df_prices, df_stock])
    print('{} stocks out of {} downloaded.'.format(count, all_number))
    print('The data set has {} rows.\n'.format(len(df_prices.index)))
    count += 1

print(df_prices)

df_prices.to_csv('data/stock_prices.csv', encoding='utf-8-sig')