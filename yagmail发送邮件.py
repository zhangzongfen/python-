import yagmail

yagindex = yagmail.SMTP(user="2433@qq.com", password="21443", host="smtp.qq.com")

Yag_contents = ['邮件正文']
# yagindex.send("23432@sina.com", "yagmail主题", Yag_contents)
# 多个接收者
# yagindex.send(["23432@sina.com", "123@qq.com"], "yagmail主题", Yag_contents)

yagindex.send("23432@sina.com", "yagmail附件主题", Yag_contents, ["D:\PyCharm 2019.1.1\workspace\python自动化测试学习\JQuery定位.py"])
