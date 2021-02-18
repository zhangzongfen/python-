import time, unittest, os
from PO_selenium_demo.common.HTMLTestReportCN import HTMLTestRunner
from PO_selenium_demo.common.helper import *
from PO_selenium_demo.page.loginpage import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail(file_new):
    f = open(file_new, "rb")
    mail_body = f.read()
    f.close()
    smtpsever = 'smtp.qq.com'
    sender = "1332029758@qq.com"
    psw = "aiafuuuiregigijd"
    receiver = "zhang_zong_fen@sina.com"
    port = 465

    msg = MIMEMultipart()
    msg['subject'] = Header(u'Page Object 自动化测试报告表', 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver

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
    print("发送成功")


def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)
    lists.sort()
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(result_dir, file[-1])
    return file_path


def getAllCases():
    Testsuit = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__), "testCases"),
                                                   pattern='test*.py')
    return Testsuit


def RunMain():
    fp = open(os.path.join(os.path.dirname(__file__), "report",
                           time.strftime("%Y-%m-%d-%H-%M-%S") + "report.html"), "wb")
    HTMLTestRunner(stream=fp, title='python + selenium 自动化测试', description="Python语言实现") \
        .run(getAllCases())


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(base_dir, 'testCases')
    test_report = os.path.join(base_dir, 'report')
    RunMain()
    new_report = new_file(test_report)
    send_mail(new_report)

