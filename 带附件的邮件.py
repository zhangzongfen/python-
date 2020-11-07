import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpsever = 'smtp.qq.com'
sender = "1332029758@qq.com"
psw = "aiafuuuiregigijd"
receiver = "zhang_zong_fen@sina.com"
port = 465

filepath = r"readme.txt"
with open(filepath, 'rb') as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = '带附件邮件测试'

body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename='test_report.html'"
msg.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpsever)
    smtp.login(sender, psw)

except:
    smtp = smtplib.SMTP_SSL(smtpsever, port)
    smtp.login(sender, psw)

smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
