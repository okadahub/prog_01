import pandas as pd
import numpy as np
import os
import glob

import matplotlib.pyplot as plt
import matplotlib.dates as dt #日時
from matplotlib.ticker import MultipleLocator # 補助目盛用

import japanize_matplotlib # 日本語表示
import pandas_datareader.data as web
import datetime

from my_module import get_filelist
from my_module import line_send_image

# インポートファイルの保管フォルダとエクスポートするフォルダのパス設定
importfile_path = ('C:\\Users\\Okada_S8\\Documents'
                   '\\32_Python\\01_sample_Data\\kabu')
export_file_path = ('C:\\Users\\Okada_S8\\Documents'
                    '\\32_Python\\02_output_Data\\kabu')


# 今日の日付取得(ファイル名追加用)
time = datetime.datetime.now()
time_day = time.strftime('%Y%m%d')
# today = datetime.datetime.today().strftime('%Y%m%d')

# ファイルリスト取得・GUIで選択
# file_list = get_filelist.main()
# print(file_list)

# ファイルリスト取得・変数指定
path = importfile_path + '\\'  +  '*.xlsx' 
file_list = glob.glob(path)
# print(file_list)

# ファイル読み込み＆データフレーム作成
# skiprows = 1
# index_col = 0
# parse_dates = False
# df = get_filelist.get_filedata(file_list,
#                       skiprows,index_col,parse_dates)

# クラスでデータ読み込み設定を登録
class DataCreate:
    def __init__(self): # ,file_list,skiprows,index_col,parse_dates):
        self.no = ''
        self.file_list = [] # file_list
        self.skiprows = 0 # skiprows
        self.index_col = 0 # index_col
        self.parse_dates = False # parse_dates
        self.default_text1 = ''
        self.default_text2 = ''
        self.msg_font = 'BIZ UDゴシック'
        self.msg_size =16
    
    def SetD(self,no,skiprows,index_col,parse_dates):
        self.no = no
        self.skiprows = skiprows
        self.index_col = index_col
        self.parse_dates = parse_dates
    
    def PathOutput(self,export_file_path,time_day):
        path = export_file_path +'\\' + self.no + '_' + time_day + '.xlsx'
        return path

data_01 = DataCreate()
# 保有株価リスト読み込み変数設定
data_01.SetD('data_01',1,0,False)
# 読み込み
df = get_filelist.get_filedata(file_list,
                                data_01.skiprows,
                                data_01.index_col,
                                data_01.parse_dates)
#　ファイル出力
# output_file = export_file_path +'\\' + 'df_base_' + time_day + '.xlsx'
# output_file = data_01.PathOutput(export_file_path,time_day)
df.to_excel(data_01.PathOutput(export_file_path,time_day))     # ファイル出力
# print(df.index)

# 読み込むコード　.T追加
data_02 = DataCreate()
data_02.no = 'data_02'
df2 = df[df['集合'] == '〇']
df2['code_T']=df2['コード'] 
for i in range(len(df2)):
    df2['code_T'].iloc[i] = str(df2['code_T'].iloc[i])  + '.T'
df2.to_excel(data_02.PathOutput(export_file_path,time_day))     # ファイル出力

# 株価情報取得
data_03 = DataCreate()
data_03.no = 'data_03'
type_a = df2['code_T'].unique() #一意のコード抽出 
type_b = df2['銘柄'].unique()   # 一意のコード抽出

# 取得データの開始日設定
data_03.default_text1 = '取得開始日入力'
data_03.default_text2 = '2021-06-01'
start_day = get_filelist.input_text(data_03.default_text1,
                            data_03.default_text2,
                            data_03.msg_font,data_03.msg_size)

# 株価情報の読み込み
df_price_all = web.DataReader(type_a, data_source='yahoo', 
                              start=start_day)
df_stock_all_close = df_price_all["Close"]
df_stock_all_close.to_excel(
            data_03.PathOutput(export_file_path,time_day))
#修正時など、株価データを読み込んでデバッグ時につかう
# data2_path_2 = r"C:\Users\Okada_S8\Documents\32_Python\02_output_Data\kabu\data_03_20220406.xlsx"
# df_stock_all_close = pd.read_excel(data2_path_2,header=[0,1],index_col=0) 

# データ加工
data_04 = DataCreate()
data_04.no = 'data_04'

df_max = df_stock_all_close. max().round(1)
df_min = df_stock_all_close. min().round(1)
df_start = pd.DataFrame(df_stock_all_close.iloc[0]).round(1)
df_recentry = pd.DataFrame(df_stock_all_close.iloc[-1]).round(1)

df_re = pd.DataFrame()
df_re['max'] = df_max
df_re['min'] = df_min
df_re['max-min'] = df_max - df_min
df_re['start'] = df_start
df_re['recentry'] = df_recentry
df_re['start_re'] = df_re['start'] - df_re['min']
df_re['recentry_re'] = df_re['recentry'] - df_re['min']
df_re['sa_now'] =  df_re['max-min'] - df_re['recentry'] 
df_re['start_re_per'] = (
        df_re['start_re'] / df_re['max-min'] *100).round(1)
df_re['recentry_re_per'] = (
        df_re['recentry_re'] / df_re['max-min'] *100).round(1)

df_re.to_excel(data_04.PathOutput(export_file_path,time_day))     # ファイル出力


# 現在株価を data_02 に追加
data_05 = DataCreate()
data_05.no = 'data_05'
df2['recentry'] = 0.0
for i in range(len(df2)):
    df2['recentry'].iloc[i] = df_re.loc[df2['code_T'].iloc[i],'recentry']

df2.to_excel(data_05.PathOutput(export_file_path,time_day))     # ファイル出力


# 月末株価推移のデータフレーム新規作成
data_06 = DataCreate()
data_06.no = 'data_06'
year_index = df_stock_all_close.index.year.unique()
year_index_start = year_index[0]
year_index_end = year_index[-1]
month_index_start = df_stock_all_close.index[0].month
month_index_end = df_stock_all_close.index[-1].month
df_month = pd.DataFrame()
for i in year_index:
    if i == year_index_start:
        for j in range(month_index_start,13):
            df_year_a = df_stock_all_close[df_stock_all_close.index.year == i]
            df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
            df_month = pd.concat([df_month,df_month_000], axis=1)  
    elif i==year_index_end:
        for j in range(1,month_index_end):
            df_year_a = df_stock_all_close[df_stock_all_close.index.year == i]
            df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
            df_month = pd.concat([df_month,df_month_000], axis=1)              
    else:
        for j in range(1,13):
            df_year_a = df_stock_all_close[df_stock_all_close.index.year == i]
            df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
            df_month = pd.concat([df_month,df_month_000], axis=1)          
            
df_month.to_excel(data_06.PathOutput(export_file_path,time_day))     # ファイル出力

