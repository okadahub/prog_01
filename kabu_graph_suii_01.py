import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt #日時
from matplotlib.ticker import MultipleLocator # 補助目盛用
import japanize_matplotlib # 日本語表示



impfl_path = r"C:\Users\Okada_S8\Documents\32_Python\02_output_Data\kabu\data_08b_20220415.xlsx"
outfl_path = r"C:\Users\Okada_S8\Documents\32_Python\02_output_Data\kabu\data_graph_kobetu_suii_01.jpg"
df = pd.read_excel(impfl_path,index_col=0,parse_dates = True)

graph_col = 3
col_all = len(df.columns)
graph_lin = int(round(col_all / graph_col,0))
graph_wh = graph_col * graph_lin
x=df.index


fig = plt.figure(constrained_layout = True,figsize=(10,50))#figsize=(10,60), ) # 全体サイズ

fig.suptitle('株価')#'株価 \n (過去保有含む個別推移)',fontsize=16)

for i in range(col_all):
    ax = fig.add_subplot(graph_lin, graph_col, i + 1) 
    ax.plot( df.iloc[:,i],linewidth=0.2 ,color='blue', linestyle='solid')

    ax.minorticks_on() 
    ax.grid(axis='x',linewidth=0.2, alpha=0.8,linestyle='solid')
    ax.grid(axis='y',linewidth=0.2, alpha=1,linestyle='solid')
    #ax.grid(axis="y",which="minor",alpha=0.5,linewidth = 0.5, linestyle="--",direction="in") # 補助目盛の線種指定
    ax.tick_params(axis='x', labelsize=8, labelrotation=30 ,direction="in" ) # 目盛りラベルのフォントサイズを設定する
    ax.tick_params(axis='y', labelsize=10 ,direction="in")# 目盛りラベルのフォントサイズを設定する

    ax.xaxis.set_major_formatter(dt.DateFormatter('%y%m%d')) # 横軸の日付表示の設定
    ax.set_title(df.columns[i].format(i))
    

plt.savefig(outfl_path, bbox_inches='tight')