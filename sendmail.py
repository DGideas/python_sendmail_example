import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'dgideas@outlook.com'
receivers = ['dgideas@outlook.com']

message = MIMEText('你好，世界', 'plain', 'utf-8')
message["From"] = Header("dgideas@outlook.com")
message["To"] = Header("DGideas <dgideas@outlook.com>")
message['Subject'] = Header('Hello world', 'utf-8')

try:
	mailServer = smtplib.SMTP('smtp.office365.com', 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login('dgideas@outlook.com', 'password')
	print(message.as_string())
	mailServer.sendmail('dgideas@outlook.com', 'dgideas@outlook.com', message.as_string())
	mailServer.quit()
except Exception:
	print("Encountered an exception.")
