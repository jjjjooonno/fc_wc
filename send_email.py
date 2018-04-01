import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
from pandas import *
email_user = 'jjjjooonno@gmail.com'
email_password = 'ehdtn0*0*'
email_send = 'jjjjooonno@gmail.com'

subject = 'test1'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = '파이썬으로 파일보내기 테스트'
msg.attach(MIMEText(body,'plain'))
path = sys.path[1]+'/'
filename='커리큘럼 정리 20180317.xlsx'
attachment  =open(path+filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment", filename= filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()