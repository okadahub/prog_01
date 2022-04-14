from numpy import append
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator # 補助目盛用
import japanize_matplotlib # 日本語表示


def plthako_single(df,col):
    fig, ax1 = plt.subplots(figsize=(9, 6))
    # ax1 = df[col[5]].boxplot(patch_artist=True)
    quant_a = len(col)
    print(quant_a)
    data = pd.DataFrame()
    for i in range(0,quant_a):
        data = pd.concat([data,df[col[i]]],axis=1)
        # print(col[i])
        # print(df[col[i]])
    # print(data)
    ax1.boxplot(data,patch_artist=True, labels=col)
    ax1.tick_params(axis='x',
                labelsize=14 , labelrotation=90 )
    
    # for i in range(0,quant_a):
    #     ax1.boxplot(df[col[i]],patch_artist=True, 
    #             labels=[i])
    # ax1.boxplot(df,patch_artist=True, labels=[col])
    plt.show()
    return


def plt_hako_comp(df1,col1,df2,pct_path):
    fig, ax1 = plt.subplots(figsize=(16, 5))
    # ax1 = df[col[5]].boxplot(patch_artist=True)
    quant_a = len(col1)
    # print(quant_a)
    data = pd.DataFrame()
    for i in range(0,quant_a):
        data = pd.concat([data,df1[col1[i]]],axis=1)
        # print(col[i])
        # print(df[col[i]])
    # print(data)
    ax1.boxplot(data,patch_artist=True, labels=col1)
    ax1.tick_params(axis='x',
                labelsize=12 , labelrotation=90 )
    ax1.tick_params(axis='y',
                labelsize=12  )
    
    ax1.grid(axis="y",which="major",
             alpha=0.6,linewidth = 1, linestyle="-")
    ax1.grid(axis="x",which="major",
             alpha=0.6,linewidth = 0.3, linestyle="-")
    ax1.minorticks_on()                                 # 補助目盛表示 ON
    ax1.xaxis.set_minor_locator(MultipleLocator(100))   # 補助目盛の目盛間隔指定
    ax1.grid(axis="y",which="minor",
             alpha=0.3,linewidth = 0.5, linestyle="--") # 補助目盛の線種指定
    quant_b = len(df2)  + 1 
    ax1.scatter(
        list(range(1,quant_b)),
        df2,
        s=200,marker='$〇$',c='orangered',
        zorder=3
    )
    plt.subplots_adjust(bottom=0.3)
    plt.savefig(pct_path, bbox_inches='tight')
    plt.show()
    
    return





def ex():
    fig, ax1 = plt.subplots(figsize=(9, 6))
    ax1 = df.boxplot(patch_artist=True)

    ax1.scatter(
        list(range(1, df.shape[1]+1)) , # == [1, 2, 3]
        df_now1[df_now1.index == "now1"],
        color="salmon",
        label="Efficiency",
        zorder=3)
    plt.show()
    
    return




if __name__ == '__main__':
    df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                    columns=['col01','col02','col03'],
                    index=['idx01','idx02','idx03'])
    df_now1 = pd.DataFrame([[6,5,4]],columns=['col01',
                    'col02','col03'],index=['now1'])
    
