import smtplib
import unittest
import os
from email.header import Header
from email.mime.text import MIMEText
from lib.HTMLTestRunner import HTMLTestRunner
import importlib, sys
importlib.reload(sys)
def send_mail(path):
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = '17600186196@163.com'
    msg['To'] = '17600186196@163.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login('17600186196@163.com', 'abc123456')
    smtp.sendmail('17600186196@163.com', '17600186196@163.com', msg.as_string())
    smtp.quit()

    print('发送成功!')

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./scripts', 'test*.py')

    base_path = os.path.dirname(__file__)
    path = base_path + "/reports/report" + ".html"
    file = open(path, 'wb')
    HTMLTestRunner(file, 1, "测试报告", "测试环境:appium Server 2018").run(suite)
    file.close()
    send_mail(path)







