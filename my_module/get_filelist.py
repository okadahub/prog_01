import PySimpleGUI as sg
from pathlib import Path
import glob

def get_path(input_data):
    text=input_data
    fpath = sg.popup_get_folder('フォルダを選択してください',
                                initial_folder=Path.cwd())
    return fpath

def get_list(folder_path,input_data):
    file_path = folder_path + '/*' + input_data
    file_list =glob.glob(file_path)
    return file_list

def pop_msg(msg):
    sg.popup(msg)

def pop_msg2(msg,msg_font,msg_size):
    sg.popup(msg,font = (msg_font,msg_size))

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
            return file_list                    
        if event==sg.WIN_CLOSED:
            break
        # if event=='-SUBMIT3-':
        #     window.close


    window.close
    

if __name__ == '__main__':
    main()
