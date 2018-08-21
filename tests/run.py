# coding=utf-8

import smtplib
import unittest
import os
import time
from email.header import Header
from email.mime.text import MIMEText

import tests
from lib.HTMLTestRunner import HTMLTestRunner

import importlib, sys

importlib.reload(sys)


def send_mail(path):
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("测试报告", 'utf-8')
    msg['From'] = '17600186196@163.com'
    msg['To'] = '17600186196@163.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login('17600186196@163.com', 'abc123456')
    smtp.sendmail('17600186196@163.com', '17600186196@163.com', msg.as_string())


    #smtp.connect("smtp.caixin.net")
    #smtp.login('tiantianchai@caixin.com', 'TKxh@#0956')
    #smtp.sendmail('tiantianchai@caixin.com', 'tiantianchai@caixin.com', msg.as_string())
    smtp.quit()

    print('邮件发送成功!')


if __name__ == '__main__':
    # str 是String  f是format格式
    # strftime()通过这个方法可以定义时间的格式
    # Y year年, m month月, d day日, H hour 小时, M minute分, S second秒


    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    #
    suite = unittest.defaultTestLoader.discover('./tests', 'test*.py')

    # suite=unittest.TestSuite()
    #
    # suite.addTest(scripts.test_login("test_allnotes"))


    # unittest.TextTestRunner() 文本测试用运行器
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path, 'wb')
    HTMLTestRunner(file, 1, "测试报告", "测试环境:Window Server 2008 + Chrome").run(suite)
    file.close()
    send_mail(path)








