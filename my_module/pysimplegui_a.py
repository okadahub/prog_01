import PySimpleGUI as sg
from pathlib import Path
import glob
import pandas as pd

def get_path(input_data):
    text=input_data
    fpath = sg.popup_get_folder('フォルダを選択してください',
                                initial_folder=Path.cwd())
    return fpath

def get_list(folder_path,input_data):
    file_path = folder_path + '/*' + input_data
    file_list =glob.glob(file_path)
    return file_list

def input_text(default_text1,default_text2,msg_font,msg_size):
    layout = [
    [sg.Text(default_text1),sg.InputText(default_text=default_text2,
                    size =(30 ,1) , text_color = '#1007b8',
                    background_color ='#def0fc',key='-TEXT-',
                    font = (msg_font,msg_size))],
    [sg.Button('実行',key='-SUBMIT-')]
    ]
    window = sg.Window('入力app',layout,size=(350,200))
    while True:
        event,values = window.read()
        if event=='-SUBMIT-':
            inpit_text = values['-TEXT-']
            # print(inpit_text)
            window.close()
            return inpit_text
        if event==sg.WIN_CLOSED:
            break
    window.close()

def input_text2(default_text1,default_text2,msg_font,msg_size):
    layout = [
    [sg.Text(default_text1)],
    [sg.InputText(default_text=default_text2,
                    size =(30 ,1) , 
                    key='-TEXT-',
                    font = (msg_font,msg_size))],
    [sg.Button('実行',key='-SUBMIT-')]
    ]
    window = sg.Window('入力app',layout,size=(350,200),
                       no_titlebar=True,
                       keep_on_top=True,
                       auto_close=False
                       )
    
    while True:
        event,values = window.read()
        if event=='-SUBMIT-':
            inpit_text = values['-TEXT-']
            # print(inpit_text)
            window.close()
            return inpit_text
        if event==sg.WIN_CLOSED:
            break
    window.close()



def pop_msg(msg):
    sg.popup(msg,
            keep_on_top=True,
            auto_close=False)

def pop_msg2(msg,msg_font,msg_size):
    sg.popup(msg,font = (msg_font,msg_size),
             keep_on_top=True,
             auto_close=False)


def get_filedata(file_list,skiprows,index_col,parse_dates):
    # print(file_list)
    df_concat = pd.DataFrame()
    # ファイル読み込み＆結合　データフレーム作成
    for i in file_list:
        df_read_excel = pd.read_excel(i,
                          skiprows=skiprows,
                          index_col=index_col,
                          parse_dates=parse_dates)
        # print(df_read_excel.head(2))
        df_concat = pd.concat([df_read_excel,df_concat])
    return df_concat


def main():
    font01 = 'BIZ UDゴシック'
    font02 = 'Arial Narrow'

    sg.theme('BluePurple')
    
    layout = [
        [sg.Text('データ保存フォルダを指定してください',
            font=(font01,18))],
        [sg.Button('フォルダ選択',key='-SUBMIT1-',
            pad=((120,0),(0,0)))],
        [sg.Text('パス:'),sg.Text(key='-ADDRESS-',
            size=(80,1),font=(font02,12))],
        [sg.Text('拡張子:'),sg.InputText(key='-TEXT-',
            size=(20,10),default_text='.xlsx')],
        [sg.Button('読み込み',key='-SUBMIT2-',
            pad=((120,0),(0,0)))],
        [sg.Text(key='-AMOUNT-',
            size=(80,10))],
        [sg.Text(key='-MESSAGE-',
            size=(30,1))],
        # [sg.Button('閉じる',key='-SUBMIT3-',
        #     pad=((120,0),(0,0)))]
    ]

    window = sg.Window('ファイルリスト取得',layout,
                    size=(650,500),font=(font01,14))
    while True:
        event,values = window.read()
        if event=='-SUBMIT1-':
            window['-MESSAGE-'].update(value='',
                                font=(font02,12))
            input_data=values['-TEXT-']
            folder_path = get_path(input_data)
            window['-ADDRESS-'].update(value=folder_path,
                                font=(font02,12))
        if event=='-SUBMIT2-':
            file_list = get_list(folder_path,input_data)
            window['-AMOUNT-'].update(value=file_list,
                                font=(font01,10))
            window['-MESSAGE-'].update(value=f'リスト取得完了しました',
                                font=(font01,12))
            window.close()
            return file_list                    
        if event==sg.WIN_CLOSED:
            break
        # if event=='-SUBMIT3-':
        #     window.close
    window.close()
    

if __name__ == '__main__':
    default_text1 = '入力'
    default_text2 = '入力してください'
    msg_font = 'BIZ UDゴシック'
    msg_size = 16
    text_a = input_text(default_text1,default_text2,msg_font,msg_size)
    print(text_a)
    text_a = input_text_simple(default_text1,default_text2,msg_font,msg_size)
    print(text_a)
    
    main()
