import matplotlib.pyplot as plt
import matplotlib.dates as dt #日時
from matplotlib.ticker import MultipleLocator # 補助目盛用

import japanize_matplotlib # 日本語表示

import seaborn as sns
import numpy as np
import pandas as pd

import openpyxl # エクセルファイルオープン
import glob
import datetime

from my_module import get_filelist
from my_module import line_send_image

# ファイル出力フォルダ指定
export_file_path = r'C:\Users\Okada_S8\Desktop\output'

# 今日の日付取得(ファイル名追加用)
time = datetime.datetime.now()
time_day = time.strftime('%Y%m%d')

# ファイルリスト取得
file_list = get_filelist.main()
# print(file_list)
df_concat = pd.DataFrame()
# ファイル読み込み＆結合　データフレーム作成
for i in file_list:
    df_read_excel = pd.read_excel(i,skiprows=3,index_col=1,parse_dates=True)
    # print(df_read_excel.head(2))
    df_concat = pd.concat([df_read_excel,df_concat])

# ソート　＆　不要なデータ削除
df_concat = df_concat.sort_values('日時')
df_concat = df_concat.drop('Unnamed: 0', axis=1)

#　ファイル出力
df_concat.to_excel(export_file_path +'/' + 'data_' + time_day + '.xlsx')
# df_concat.head(2)

get_filelist.pop_msg('データフレーム作成＆ファイル出力完了しました')