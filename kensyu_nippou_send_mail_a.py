from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from datetime import datetime,timedelta

from pandas import DataFrame

import time
import pandas as pd
import numpy as np
import os
import datetime
import io
import requests

import openpyxl # エクセルファイルオープン
import glob

import subprocess
from os.path import join

# インポートファイルの保管フォルダとエクスポートするフォルダのパス設定
import_file_path = ('C:\\Users\Okada_S8\\Documents'
                      '\\32_Python\\anaconda\\etc'
                    '\\input_data_01\\mail_meitec_001.xlsx')
export_folder_path = ('C:\\Users\Okada_S8\\Documents'
                    '\\32_Python\\anaconda\\etc\\output01')

df_read_excel = pd.read_excel(import_file_path,sheet_name = 1)# ,
                              # skiprows=3,
                              # index_col=1) #   ,parse_dates=True)

df_read_excel

book = openpyxl.load_workbook(import_file_path)
sheet = book.worksheets[1]

cell = sheet['B1']
cell.value

a = sheet['B']
b = sheet['C']
c = sheet['D']

c[4].value

name_to = a[1].value
name_cc = a[2].value
kenmei = a[4].value
honbun = a[5].value
print(
name_to,'\n',
name_cc,'\n',
kenmei,'\n',
honbun
)

nameb_to = b[1].value
nameb_cc = b[2].value
kenmeib = b[4].value
honbunb = b[5].value
print(
nameb_to,'\n',
nameb_cc,'\n',
kenmeib,'\n',
honbunb
)

# クローム起動バッチファイルpath　※ポート番号を固定して起動する
path = r"C:\Users\Okada_S8\Documents\32_Python\anaconda\temp_9222\openChrome.bat"

subprocess.Popen(path)

# クロームドライバーのpath
CHROMEDRIVER = "C:\\Users\\Okada_S8\\Documents\\32_Python\\anaconda\\chromedriver.exe"

# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

time.sleep(2)
# メール新規作成ボタンを押す
frm = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button')
frm.click()

time.sleep(3)
# メール作成・件名
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input')
elem.clear()
# elem.send_keys('【提出】日報、健康観察記録表_MT03_岡田 光弘')
elem.send_keys(kenmei)

time.sleep(1)
# メール作成・本文
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div/div')
elem.clear()
elem.send_keys(honbun)

time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(name_to)

time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[6]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(name_cc)

time.sleep(2)
# メール新規作成ボタンを押す
frm = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/span/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/button')
frm.click()

time.sleep(3)
# メール作成・件名
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input')
elem.clear()
# elem.send_keys('【提出】日報、健康観察記録表_MT03_岡田 光弘')
elem.send_keys(kenmeib)

time.sleep(1)
# メール作成・本文
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div/div')
elem.clear()
elem.send_keys(honbunb)

time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(nameb_to)

time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[6]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(nameb_cc)
