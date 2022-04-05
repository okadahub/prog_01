import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import my_account as gmail # アカウント情報

def gmail_send_image(subject,mail_to,txt,image_file_path):
    # メールデータを作成 --- (*1)
    msg = MIMEMultipart()
    msg['Subject'] = subject # 件名
    msg['From'] = gmail.account_g # 送信元
    msg['To'] = mail_to # 'okadada7@gmail.com'  # 宛先
    msg.attach(MIMEText(txt))
    with open(image_file_path, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    # メール送信 --- (*4)
    send_gmail(msg)
    print("ok")

def gmail_send_msg(subject,mail_to,txt):
    # メールデータを作成 --- (*1)
    msg = MIMEMultipart()
    msg['Subject'] = subject # 件名
    msg['From'] = gmail.account_g # 送信元
    msg['To'] = mail_to # 'okadada7@gmail.com'  # 宛先
    msg.attach(MIMEText(txt))
    # メール送信 --- (*4)
    send_gmail(msg)
    print("ok")

# Gmailに接続 --- (*6)
def send_gmail(msg):
    # Gmailサーバーに接続
    server = smtplib.SMTP_SSL(
        'smtp.gmail.com', 465,
        context=ssl.create_default_context())
    server.set_debuglevel(0) # ログ出力 --- (*7)
    # ログインしてメールを送信
    server.login(gmail.account_g, gmail.password_g)
    # server.login(account, password)
    server.send_message(msg)
 

if __name__ == '__main__':
    subject = 'Pythonにてテスト送信'
    mail_to = 'okadada7@gmail.com'
    txt = '''
    テスト送信してます。
    
    pythonより
    '''
 
    image_file_path = r'C:\Users\Okada_S8\Desktop\aaa.png'
    gmail_send_msg(subject,mail_to,txt)
    gmail_send_image(subject,mail_to,txt,image_file_path)  

