from cmath import nan
import pandas as pd

def readcsv(file_name,skiprows,index_col,parse_dates):
    df =pd.read_csv(file_name,
        skiprows=skiprows,
        index_col=index_col,
        parse_dates=parse_dates)
    return df

def readexcel(file_name,skiprows,index_col,parse_dates):
    df =pd.read_excel(file_name,
        skiprows=skiprows,
        index_col=index_col,
        parse_dates=parse_dates)
    return df

# 複数ファイル・CSVファイル読み込み＆結合 データフレーム作成
def readcsvs(file_list,skiprows,index_col,parse_dates):
    print(file_list)
    print(skiprows)
    print(index_col)
    print(parse_dates)
    df_concat = pd.DataFrame()
    for i in file_list:
        df_read_excel = pd.read_excel(i,
                          skiprows=skiprows,
                          index_col=index_col,
                          parse_dates=parse_dates)
        # print(df_read_excel.head(2))
        df_concat = pd.concat([df_read_excel,df_concat])
    return df_concat

# 複数ファイル・エクセルファイル読み込み＆結合 データフレーム作成
def readexcels(file_list,skiprows,index_col,parse_dates):
    print(file_list)
    print(skiprows)
    print(index_col)
    print(parse_dates)
    df_concat = pd.DataFrame()
    for i in file_list:
        df_read_excel = pd.read_excel(i,
                          skiprows=skiprows,
                          index_col=index_col,
                          parse_dates=parse_dates)
        # print(df_read_excel.head(2))
        df_concat = pd.concat([df_read_excel,df_concat])
    return df_concat


# データフレーム 指定列の文字末に文字追加
def add_textdf(df,col,add_txt):
    for i in range(len(df)):
        df[col].iloc[i] = str(df[col].iloc[i])  + add_txt
    return df


# データフレーム 指定列に、別のデータフレームをサーチして追加
# col1 参照カラム名 col2 代入カラム名
def add_seachtextdf(df,df_from,col1,col2):
    df[col1] = 0.0
    for i in range(len(df)):
        try:
            df[col1].iloc[i] = df_from.loc[df[col2].iloc[i],col1]
        except Exception:
            df[col1].iloc[i] = None
    return df

# データフレーム インデックス変更
def dfre_index(df,text):
    if df.index.name != text:
        df = df.set_index(text)#
        # print('dfre_indexの設定')
        # print(df)
        return df
    return

# データフレーム 必要カラム抽出
def dfre_pull(df,list):
    df = df[list]#
    # print('dfre_pullの内容')
    # print(df)
    return df

# データフレーム カラム名変更
# df:変更df list:変更カラムリスト  axis:0or1
def dfre_colmns(df,list,axis):
    df = df.set_axis(list,axis = axis)
    return df

# リスト 対応リスト作成 データフレームを参照して作成
# df:参照df(indexで参照) lst_a:対応リスト
def createlst_a(df,df_col,lst_a):
    # print('createlst_aの設定')
    # print(df)
    # print(df_col)
    # print(lst_a)
    new_lst = list()
    for i in range(0,len(lst_a)):
        new_lst.append(df[df_col].loc[lst_a[i]])
    return new_lst


# データフレーム 月毎の末日のデータを抽出して作成
def df_endofmonth(df):
    year_index = df.index.year.unique() # 年 抽出
    year_index_start = year_index[0]                    # スタート年
    year_index_end = year_index[-1]                     # 終了年
    month_index_start = df.index[0].month # スタート月・スタート年
    month_index_end = df.index[-1].month  # エンド月・終了年    
    df_month = pd.DataFrame()
    for i in year_index:
        if i == year_index_start:
            for j in range(month_index_start,13):
                df_year_a = df[df.index.year == i]
                df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
                df_month = pd.concat([df_month,df_month_000], axis=1)  
        elif i==year_index_end:
            for j in range(1,month_index_end):
                df_year_a = df[df.index.year == i]
                df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
                df_month = pd.concat([df_month,df_month_000], axis=1)              
        else:
            for j in range(1,13):
                df_year_a = df[df.index.year == i]
                df_month_000 = pd.DataFrame(df_year_a[df_year_a.index.month == j].iloc[-1].round(1))
                df_month = pd.concat([df_month,df_month_000], axis=1)   
    return df_month

# データフレーム max、min、他加工
def df_maxminetc01(df):
    df_max = df. max().round(1)
    df_min = df. min().round(1)
    df_start = pd.DataFrame(df.iloc[0]).round(1)
    df_recentry = pd.DataFrame(df.iloc[-1]).round(1)
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
    return df_re






def del_colm(df,cel_txt,axis):
    num = len(cel_txt)
    for i in range(0,num):
        if cel_txt[i] in df.columns:
            df = df.drop(cel_txt[i],axis = axis)
    return df
