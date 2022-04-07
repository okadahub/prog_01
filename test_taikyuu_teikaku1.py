#import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator # 補助目盛用
#import japanize_matplotlib # 日本語表示
#import seaborn as sns
#import numpy as np
#import openpyxl # エクセルファイルオープン
#import glob
#from my_module import line_send_image

import matplotlib.dates as dt #日時
import pandas as pd
import datetime
from my_module import pysimplegui_a

class Setting:
    def __init__(self):
        self.no = ''
        self.today = datetime.datetime.now()
        self.workday = self.today.strftime('%Y%m%d')
        self.export_file_path = ('C:\\Users'
                        '\\Okada_S8\\Desktop\\output')
        self.default_path = ('C:\\Users\\Okada_S8'
                        '\\Documents\\32_Python'
                        '\\anaconda\\train001\\data01')
        self.extension = '.xlsx'
        
    def CreateDataFrame(self):
        print(self.default_path)
        print(self.extension)
        self.file_list = pysimplegui_a.filelist(
            self.default_path,self.extension)
        df_concat = pd.DataFrame()
        # ファイル読み込み＆結合　データフレーム作成
        for i in self.file_list:
            df_read_excel = pd.read_excel(i,skiprows=3,index_col=1,parse_dates=True)
            # print(df_read_excel.head(2))
            df_concat = pd.concat([df_read_excel,df_concat])
        # ソート　＆　不要なデータ削除
        df_concat = df_concat.sort_values('日時')
        df_concat = df_concat.drop('Unnamed: 0', axis=1)
        return df_concat
    
    def PathOutput(self):
        save_path = self.export_file_path +'\\' + self.no + '_' + self.workday + self.extension
        print('確認')
        print(save_path)
        return save_path

data_01 = Setting()
data_01.no = 'data_01'
df = data_01.CreateDataFrame()
df.to_excel(data_01.PathOutput())
pysimplegui_a.pop_msg('データフレーム作成＆ファイル出力完了しました')

print('成功！')