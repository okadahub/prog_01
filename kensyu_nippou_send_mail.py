#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 


# In[1]:


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


# In[ ]:





# In[2]:


# インポートファイルの保管フォルダとエクスポートするフォルダのパス設定
import_file_path = ('C:\\Users\Okada_S8\\Documents'
                      '\\32_Python\\anaconda\\etc'
                    '\\input_data_01\\mail_meitec_001.xlsx')
export_folder_path = ('C:\\Users\Okada_S8\\Documents'
                    '\\32_Python\\anaconda\\etc\\output01')


# In[3]:


# export_file_path ='C:\\Users\\Okada_S8\\Documents\\32_Python\\anaconda\\web_login\\output\\'
# export_file_path ='C:\\Users\\Okada_S8\\Desktop\\'


# In[4]:


df_read_excel = pd.read_excel(import_file_path,sheet_name = 1)# ,
                              # skiprows=3,
                              # index_col=1) #   ,parse_dates=True)


# In[5]:


df_read_excel


# In[6]:


book = openpyxl.load_workbook(import_file_path)
sheet = book.worksheets[1]


# In[7]:


cell = sheet['B1']
cell.value


# In[8]:


a = sheet['B']
b = sheet['C']
c = sheet['D']


# In[9]:


c[4].value


# In[10]:


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


# In[11]:


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


# In[ ]:





# In[12]:


# クローム起動バッチファイルpath　※ポート番号を固定して起動する
path = r"C:\Users\Okada_S8\Documents\32_Python\anaconda\temp_9222\openChrome.bat"


# In[13]:


subprocess.Popen(path)


# In[14]:


# クロームドライバーのpath
CHROMEDRIVER = "C:\\Users\\Okada_S8\\Documents\\32_Python\\anaconda\\chromedriver.exe"


# In[15]:


# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)


# In[16]:


# time.sleep(1)
# URLを指定して、新しいタブを開く
# driver.execute_script("window.open('https://outlook.office.com/mail/');")

# 開いたタブに移動する [0]が最初に開いたタブ、移行順に番号が振られる
# driver.switch_to.window(driver.window_handles[1])


# In[17]:


# driver.switch_to.window(driver.window_handles[1])


# In[ ]:





# In[18]:


time.sleep(2)
# メール新規作成ボタンを押す
frm = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button')
frm.click()


# In[19]:


time.sleep(3)
# メール作成・件名
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input')
elem.clear()
# elem.send_keys('【提出】日報、健康観察記録表_MT03_岡田 光弘')
elem.send_keys(kenmei)


# In[20]:


time.sleep(1)
# メール作成・本文
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div/div')
elem.clear()
elem.send_keys(honbun)


# In[21]:


time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(name_to)


# In[22]:


time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[6]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(name_cc)


# In[ ]:





# In[ ]:





# In[23]:


time.sleep(2)
# メール新規作成ボタンを押す
frm = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/span/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/button')
frm.click()


# In[24]:


time.sleep(3)
# メール作成・件名
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input')
elem.clear()
# elem.send_keys('【提出】日報、健康観察記録表_MT03_岡田 光弘')
elem.send_keys(kenmeib)


# In[25]:


time.sleep(1)
# メール作成・本文
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div/div')
elem.clear()
elem.send_keys(honbunb)


# In[26]:


time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(nameb_to)


# In[27]:


time.sleep(1)
# メール作成・宛先
elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[6]/div/div/div/div/div/div[1]/div/div/input')
elem.clear()
elem.send_keys(nameb_cc)


# In[ ]:





# In[ ]:





# In[ ]:




