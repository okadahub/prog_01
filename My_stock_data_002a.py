import pandas as pd
import numpy as np
import os
import glob

import matplotlib.pyplot as plt
import matplotlib.dates as dt #日時
from matplotlib.ticker import MultipleLocator # 補助目盛用

import japanize_matplotlib # 日本語表示

# パッケージ
import pandas_datareader.data as web

import datetime

# インポートファイルの保管フォルダとエクスポートするフォルダのパス設定
importfile_path = 'C:\\Users\\Okada_S8\\Documents\\32_Python\\anaconda\\train002_My_stock_price\\My_stock'
export_file_path = 'C:\\Users\\Okada_S8\\Documents\\32_Python\\anaconda\\train002_My_stock_price\\output02'

# インポートファイルのリスト取得
file_name = 'kento_20220316'
sheetnm = 'Sheet1'
import_data = importfile_path + '\\'  + file_name + '.xlsx'#+ data_name
import_data

df = pd.read_excel(import_data,index_col=1) # ,sheet_name = 'Sheet1') #シート名指定で読み込み
# df

df['code_t'] = df.index
for i in df['code_t']:
    df['code_t'][i] = str(i)  + '.T'
# df

df_re = df.reset_index().set_index('code_t')
# df_re

# 取得する株式コード設定
SYMBOLS_all = df['code_t']

# 株価情報の取得
df_stock_all = web.DataReader(SYMBOLS_all, data_source='yahoo', start='2020-12-01')

#　ファイル出力
df_stock_all.to_excel(export_file_path +'\\' + 'df_stock_all.xlsx')

# 保存した株価ファイルを読み込んで以降検討する場合
import_data_re = export_file_path +'\\' + 'df_stock_all.xlsx'
df_stock_all = pd.read_excel(import_data_re,header=[0,1],index_col=0)# skiprows=[3])# ,usecols=[0, 1, 3], skipfooter=1)
# df_stock_all

df_stock_all_close = df_stock_all["Close"]
df_stock_all_close.to_excel(export_file_path +'/' + 'df_stock_all_close.xlsx')
# df_stock_all_close.head(2)
# df_stock_all_close.tail(3)

st = df_stock_all_close['2305.T']['2020-12-01']
# df_stock_all_close['2599.T'] - a
ma = df_stock_all_close['2305.T'].max()
mi = df_stock_all_close['2305.T'].min()
en = df_stock_all_close['2305.T']['2022-03-16']
now = df_stock_all_close['2305.T']['2021-08-16']
per = ((now - mi) / (ma - mi)) * 100
print(st,
      ma,
      mi,
      en,
      now,
      per.round(1) )


standard = '2020-12-01'


df_max = df_stock_all_close. max()
df_min = df_stock_all_close. min()
df_start = pd.DataFrame(df_stock_all_close.loc['2020-12-01'])
df_tail = df_stock_all_close.tail(1).index

df_re['max'] = df_max
df_re['min'] = df_min
df_re['max-min'] = df_max - df_min
df_re['start'] = df_start
df_re['end'] = df_stock_all_close.loc[df_tail].T

df_re['start_re'] = df_re['start'] - df_re['min']
df_re['end_re'] = df_re['end'] - df_re['min']

df_re['now'] = df_re['end_re'] / df_re['max-min'] *100
df_re['start_re_per'] = df_re['start_re'] / df_re['max-min'] *100

df_re['sa_now'] =  df_re['max-min'] - df_re['end_re'] 

#　ファイル出力
# df_re.to_excel(export_file_path +'\\' + 'df_re.xlsx')


df_all_a = pd.DataFrame()

for i in df_re.index:
    a = df_stock_all_close[i][standard]
    df_all_a[i] = df_stock_all_close[i] - a
# df_all_a


df_stock_all_close['2599.T'].max()



df_all_b = pd.DataFrame()

for i in df_re.index:
    max = df_stock_all_close[i].max()
    min = df_stock_all_close[i].min()
    now = df_stock_all_close[i]
    df_all_b[i] = ( now - min ) / ( max - min ) *  100
    
#　ファイル出力
df_all_b.to_excel(export_file_path +'\\' + 'df_all_b.xlsx')   
    




df_all_b_01 = df_re.sort_values('now',ascending=False).round(1)
# df_all_b_01.head(15)



df_all_b_01['return'] = (df_all_b_01['dividend'] +  df_all_b_01['gain'] / df_all_b_01['qua']) *0.8 / df_all_b_01['end'] *100
df_all_b_01['max-end'] = df_all_b_01['max'] - df_all_b_01['end']
# df_all_b_01.round(1)


today = datetime.datetime.today().strftime('%Y%m%d')
# today

try001 = export_file_path +'\\' + 'df_all_b_01' + today + '.xlsx'
# try001


#　ファイル出力
df_all_b_01.to_excel(try001)



