import smtplib
from email.mime.text import MIMEText

smtpsever = 'smtp.qq.com'
sender = "1332029758@qq.com"
psw = "aiafuuuiregigijd"
receiver = "zhang_zong_fen@sina.com"
port = 465

msg = MIMEText("文本邮件正文", 'html', 'utf-8')
msg['from'] = '1332029758@qq.com'
msg['to'] = 'zhang_zong_fen@sina.com'
msg['subject'] = '纯文本邮件测试'

smtp = smtplib.SMTP_SSL(smtpsever, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
