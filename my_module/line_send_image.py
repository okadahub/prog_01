import requests

# アクセストークンを以下に設定
acc_token = 'x3Rh0bdBxKTiu8XBEPkcZRjcCR8xWIz0HcDjy8dKEhU'

def send_line_ms(msg):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    # サーバーへ送信 --- (*4)
    requests.post(url, headers=headers,params=payload)

def send_line_pic(msg, image_file):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    # 画像を読み込む --- (*3)
    with open(image_file, 'rb') as fp:
        files = {'imageFile': fp}
        # サーバーへ送信 --- (*4)
        requests.post(url, headers=headers, 
            params=payload, files=files)

if __name__ == '__main__':
    import datetime
    image_file = ('C:\\Users\\Okada_S8\\'
              'Documents\\32_Python\\anaconda\\'
              'web_login\\output\\Yutai_point_20220318.png')
    time = datetime.datetime.now()
    time_send = time.strftime('%Y/%m/%d')          
    msg1 = '今日は' + time_send + 'です～！！！'
    msg2 = '宮、かっぱ寿司の' + time_send + '時点のポイント連絡です～！！！'
    send_line_ms(msg1)
    send_line_pic(msg2,image_file)
    print('ok')