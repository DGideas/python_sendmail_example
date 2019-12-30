import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'dgideas@outlook.com'
receivers = ['dgideas@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
#message['From'] = Header("菜鸟教程", 'utf-8')     # 发送者
#message['To'] =  Header("测试", 'utf-8')          # 接收者
message["From"] = Header("dgideas@outlook.com")
message["To"] = Header("DGideas <dgideas@outlook.com>")
message['Subject'] = Header('来自SMTP的问候……', 'utf-8')
#message['Subject'] = Header(subject, 'utf-8')

try:
	mailserver = smtplib.SMTP('smtp.office365.com', 587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('dgideas@outlook.com', 'password')
	print(message.as_string())
	mailserver.sendmail('dgideas@outlook.com','dgideas@outlook.com', message.as_string())
	mailserver.quit()
except Exception:
	print("Encountered an exception.")
