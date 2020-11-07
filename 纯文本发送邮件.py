import smtplib
from email.mime.text import MIMEText

smtpsever = 'smtp.qq.com'
sender = "1238@qq.com"
psw = "235435"
receiver = "3244@sina.com"
port = 465

msg = MIMEText("文本邮件正文", 'html', 'utf-8')
msg['from'] = '1238@qq.com'
msg['to'] = '3244@sina.com'
msg['subject'] = '纯文本邮件测试'

smtp = smtplib.SMTP_SSL(smtpsever, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
