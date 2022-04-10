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

from my_module import pysimplegui_a
from my_module import line_send_image

# クラスでデータ読み込み設定を登録
class DataCreate:
    def __init__(self):
        self.no = ''
        self.today = datetime.datetime.now()
        self.workday = self.today.strftime('%Y%m%d')
        self.file_list = [] # file_list
        self.skiprows = 0 # skiprows
        self.index_col = 0 # index_col
        self.parse_dates = False # parse_dates
        self.default_text1 = ''
        self.default_text2 = ''
        self.msg_font = 'BIZ UDゴシック'
        self.msg_size =16
        self.exportfile_path = ('C:\\Users\\Okada_S8'
                        '\\Documents\\32_Python'
                        '\\02_output_Data\\kabu')
        self.readfile_path = ('C:\\Users\\Okada_S8'
                        '\\Documents\\32_Python'
                        '\\01_sample_Data\\kabu')
        self.extension = '.xlsx'
    
    
    def SetD(self,no,skiprows,index_col,parse_dates):
        self.no = no
        self.skiprows = skiprows
        self.index_col = index_col
        self.parse_dates = parse_dates
    
    
    def CreateDataFrame(self):
        read_path = self.readfile_path +'\\' + 'Book_20220406.xlsx'
        print(read_path)
        df = pysimplegui_a.readexcel(
            read_path,self.skiprows,
            self.index_col,self.parse_dates )
        print(df)
        return df
    
    
    def PathOutput(self):
        path = self.exportfile_path +'\\' + self.no + '_' + self.workday + '.xlsx'
        return path


data_01 = DataCreate()
data_01.exportfile_path
data_01.readfile_path

data_01.SetD('data_01',1,0,False) # 読み込み変数設定
df = data_01.CreateDataFrame()    # データフレーム作成
df.to_excel(data_01.PathOutput()) # ファイル出力


# 読み込むコード .T追加
data_02 = DataCreate()
data_02.no = 'data_02'
df2 = df[df['集合'] == '〇'] # 読み込み行のみ抽出
df2['code_T']=df2['コード']  # .T列準備
for i in range(len(df2)):
    df2['code_T'].iloc[i] = str(df2['code_T'].iloc[i])  + '.T'
df2.to_excel(data_02.PathOutput())  # ファイル出力

# 株価情報取得準備
data_03 = DataCreate()
data_03.no = 'data_03'
type_a = df2['code_T'].unique() #一意のコード抽出 
type_b = df2['銘柄'].unique()   # 一意のコード抽出

# 取得データの開始日設定
data_03.default_text1 = '取得開始日入力'
data_03.default_text2 = '2021-06-01'
start_day = pysimplegui_a.input_text(data_03.default_text1,
                            data_03.default_text2,
                            data_03.msg_font,data_03.msg_size)

# 株価情報の読み込み
# df_price_all = web.DataReader(type_a, data_source='yahoo', 
#                               start=start_day)
# df_stock_all_close = df_price_all["Close"]
# df_stock_all_close.to_excel(data_03.PathOutput())  # ファイル出力
#修正時など、株価データを読み込んでデバッグ時につかう
data2_path_2 = (r"C:\Users\Okada_S8\Documents\32_Python\01_sample_Data\kabu\data_03.xlsx")
df_stock_all_close = pd.read_excel(data2_path_2,header=[0,1],index_col=0) 

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

df_re.to_excel(data_04.PathOutput())  # ファイル出力

# 現在株価を data_02 に追加
data_05 = DataCreate()
data_05.no = 'data_05'
df2['recentry'] = 0.0
for i in range(len(df2)):
    df2['recentry'].iloc[i] = df_re.loc[df2['code_T'].iloc[i],'recentry']

df2.to_excel(data_05.PathOutput())  # ファイル出力


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
            
df_month.to_excel(data_06.PathOutput())  # ファイル出力