# import numpy as np
# import os
# import glob
# import matplotlib.pyplot as plt
# import matplotlib.dates as dt #日時
# from matplotlib.ticker import MultipleLocator # 補助目盛用
# import japanize_matplotlib # 日本語表示
# from sqlalchemy import column
# from my_module import line_send_image

import pandas_datareader.data as web
import pandas as pd
import datetime
from my_module import pysimplegui_a
from my_module import make_data
from my_module import graph_plot_a
from my_module import make_data

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
        self.extpic = 'jpg'
        self.initialfilename = 'Book_20220412'
        self.reloadfilename = 'data_03_20220414'
    
    def SetFformat(self,extension,extpic):
        self.extension = extension
        self.extpic = extpic
        return
    
    def SetD(self,no,skiprows,index_col,
             parse_dates):
        self.no = no
        self.skiprows = skiprows
        self.index_col = index_col
        self.parse_dates = parse_dates
        return
    
    def CreateFstdf(self):
        read_path = ( self.readfile_path 
            +'\\' + self.initialfilename 
            + self.extension)
        print(read_path)
        df = pysimplegui_a.readexcel(
            read_path,self.skiprows,
            self.index_col,self.parse_dates )
        # print(df)
        return df
    
    def SaveExcelPath(self):
        path = (self.exportfile_path 
            +'\\' + self.no + '_' 
            + self.workday + self.extension)
        return path
    
    def SaveGraphPath(self):
        path = (self.exportfile_path 
            +'\\' + self.no + '_' 
            + self.workday + self.extpic)
        return path
    
    def GraphParam(self,max,max2):
        self.max = max
        self.max2 = max2
        return
    
    def OutPath(self,ext):
        path = (self.exportfile_path 
            +'\\' + self.no + '_' 
            + self.workday + ext)
        return path
    
    def get_price(self,code_list):
        self.text= 'yes:株価取得？ or no:既存データ読み込み'
        value = pysimplegui_a.how_ok(
            self.text,self.msg_font,self.msg_size)
        if value == 'OK':
            start_day = pysimplegui_a.input_text(
                data_03.default_text1,
                data_03.default_text2,
                data_03.msg_font,data_03.msg_size)
            # 株価情報の読み込み
            df = web.DataReader(
                code_list, data_source='yahoo', 
                start=start_day)
            df = df["Close"]
            return df
        else:
            #修正時など、株価データを読み込んでデバッグ時につかう
            path = (self.readfile_path 
            +'\\' + self.reloadfilename + self.extension)
            # print(path)
            df = pd.read_excel(path,header=[0],index_col=0) 
            return df


fl_format = DataCreate()
fl_format.SetFformat('.xlsx','jpg')

data_01 = DataCreate()
data_01.SetD('data_01',1,0,False)   # 読み込み変数設定
df = data_01.CreateFstdf()          # 読み込みリスト用DF作成
# df.to_excel(data_01.SaveExcelPath())   # ファイル出力

data_02 = DataCreate()
data_02.no = 'data_02'
df2 = df[df['集合'] == '〇']        # 読み込み行のみ抽出
df2['code_T']=df2['コード']         # .T列用の列追加
df2a = make_data.add_textdf(df2,'code_T','.T') # .T文字追加
df2a = df2a.sort_values(
    by='コード',ascending=False)    # ソート
df2a.to_excel(data_02.SaveExcelPath()) # ファイル出力

# 株価情報取得準備
data_03 = DataCreate()
data_03.no = 'data_03'
type_a = df2a['code_T'].unique() #一意のコード抽出 
type_b = df2a['銘柄'].unique()   # 一意のコード抽出
# quant_a = len(type_a)
# 取得データの開始日設定
data_03.default_text1 = '取得開始日入力'
data_03.default_text2 = '2021-06-01'
df_price = data_03.get_price(type_a) # 株価取得
df_price.to_excel(data_03.SaveExcelPath())  # ファイル出力
# df_pclose = df_price.copy()

# データ加工 max,min 集計df新規作成
data_04 = DataCreate()
data_04.no = 'data_04'
df4 = make_data.df_maxminetc01(df_price)
df4.to_excel(data_04.SaveExcelPath())  # ファイル出力


data_05 = DataCreate()
data_05.no = 'data_05'
df5 = df2.copy()
df5['recentry'] = 0.0
df_from = df4.copy()
col1 = 'recentry'
col2 = 'code_T'
df5a = make_data.add_seachtextdf(
    df5,df_from,col1,col2)
df5a.to_excel(data_05.SaveExcelPath())  # ファイル出力

# 月末株価推移のデータフレーム新規作成・家計集計用
data_06 = DataCreate()
data_06.no = 'data_06'
df_pclose_a = df_price.copy()
df_month_b =  make_data.df_endofmonth(
    df_pclose_a)
df_month_b.to_excel(data_06.SaveExcelPath())  # ファイル出力




# グラフ作成 準備
data_07 = DataCreate()
data_07.no = 'data_07'
data_07.GraphParam(2000,5000)
a = int(data_07.max)
b = int(data_07.max2)
df7_4 = df4.copy()
df7_p = df_price.copy()
df7_4 = df7_4.sort_values(
    by='recentry_re_per',ascending=False)
col_data7a = df7_4.index.unique()

# グラフ作成1
data_08a = DataCreate()
data_08a.no = 'data_08a'
area_a = df7_p.max() > 0
area_a = df7_p.max() < a
df8_pa = df7_p[
    df7_p.columns[area_a]].round(1)
col_data8aa = df8_pa.columns.unique()
list_a = set(col_data7a)^set(col_data8aa)
list_a = list(list_a)
df8aa = make_data.del_colm(df8_pa,list_a,1)
df8ba =  make_data.del_colm(df7_4,list_a,0)
col_data8ba = df8ba.index.unique()
df8aa = df8aa.reindex(columns=col_data8ba)
# df8aa.to_excel(data_07.SaveExcelPath())  # ファイル出力

# グラフ作成 ラベル名を銘柄に変更
re_no = 'code_T'
df8ca = make_data.dfre_index(df5a,re_no)
re_col = '銘柄'
df08_recol = [re_col]
df8ea = make_data.dfre_pull(df8ca,df08_recol)
colm_df8a = df8aa.columns# 
new_col = make_data.createlst_a(df8ea,re_col,colm_df8a)
newcol_axis = 1
df8da = make_data.dfre_colmns(df8aa,new_col,newcol_axis)
df8da.to_excel(data_08a.SaveExcelPath())  # ファイル出力
df_ry8 = pd.DataFrame(df8da.iloc[-1]).round(1)# グラフに重ねるデータ 現在株価(点)
graph_plot_a.plt_hako_comp(
    df8da,new_col,df_ry8,data_08a.SaveGraphPath()) # グラフ出力

# グラフ作成2
data_08b = DataCreate()
data_08b.no = 'data_08b'
area_b = df7_p.max() > a
area_b = df7_p.max() < b
df8_pb = df7_p[
    df7_p.columns[area_b]].round(1)
col_data8ab = df8_pb.columns.unique()
list_b = set(col_data7a)^set(col_data8ab)
list_b = list(list_b)
df8ab = make_data.del_colm(df8_pb,list_b,1)
df8bb =  make_data.del_colm(df7_4,list_b,0)
col_data8bb = df8bb.index.unique()
df8ab = df8ab.reindex(columns=col_data8bb)
# df8ab.to_excel(data_07.SaveExcelPath())  # ファイル出力

# グラフ作成 ラベル名を銘柄に変更
re_no = 'code_T'
df8cb = make_data.dfre_index(df5a,re_no)
re_col = '銘柄'
df08_recol = [re_col]
df8eb = make_data.dfre_pull(df8cb,df08_recol)
colm_df8b = df8ab.columns# 
new_col = make_data.createlst_a(df8eb,re_col,colm_df8b)
newcol_axis = 1
df8db = make_data.dfre_colmns(df8ab,new_col,newcol_axis)
df8db.to_excel(data_08b.SaveExcelPath())  # ファイル出力
df_ry8 = pd.DataFrame(df8db.iloc[-1]).round(1)# グラフに重ねるデータ 現在株価(点)
graph_plot_a.plt_hako_comp(
    df8db,new_col,df_ry8,data_08b.SaveGraphPath()) # グラフ出力


# グラフ作成3
data_08c = DataCreate()
data_08c.no = 'data_08c'
area_c = df7_p.max() < 350000
area_c = df7_p.max() > b
df8_pc = df7_p[
    df7_p.columns[area_c]].round(1)
col_data8ac = df8_pc.columns.unique()
list_c = set(col_data7a)^set(col_data8ac)
list_c = list(list_c)
df8ac = df8_pc.copy()
df8ac = make_data.del_colm(df8_pc,list_c,1)
df4c =  make_data.del_colm(df7_4,list_c,0)
col_data04a = df4c.index.unique()
df8ac = df8ac.reindex(columns=col_data04a)
# df8ac.to_excel(data_04b.SaveExcelPath())  # ファイル出力

# グラフ作成 ラベル名を銘柄に変更
re_no = 'code_T'
df8cc = make_data.dfre_index(df5a,re_no)
re_col = '銘柄'
df08_recol = [re_col]
df08ac = make_data.dfre_pull(df8cc,df08_recol)
colm_df8c = df8ac.columns# 
new_col = make_data.createlst_a(df08ac,re_col,colm_df8c)
newcol_axis = 1
df8ac = make_data.dfre_colmns(df8ac,new_col,newcol_axis)
# df8ac.to_excel(data_09.SaveExcelPath())  # ファイル出力
df_ry8 = pd.DataFrame(df8ac.iloc[-1]).round(1)# グラフに重ねるデータ 現在株価(点)
graph_plot_a.plt_hako_comp(
    df8ac,new_col,df_ry8,data_08c.SaveGraphPath()) # グラフ出力

