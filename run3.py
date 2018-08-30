# coding=utf-8

import smtplib
import unittest
# HTMLTestRunner是基于unittest框架的一个扩展, 可以自己在网上自行下载
import os
import time
from email.header import Header
from email.mime.text import MIMEText

import scripts
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
    # smtp.connect("smtp.163.com")
    # smtp.login('17600186196@163.com', 'abc123456')
    # # 注意msg是MIME类型,需要转成String类型再发送
    # smtp.sendmail('17600186196@163.com', '17600186196@163.com', msg.as_string())


    smtp.connect("smtp.caixin.net")
    smtp.login('tiantianchai@caixin.com', 'TKxh@#0956')
    smtp.sendmail('tiantianchai@caixin.com', 'tiantianchai@caixin.com', msg.as_string())
    smtp.quit()

    print('邮件发送成功!')


if __name__ == '__main__':
    # str 是String  f是format格式
    # strftime()通过这个方法可以定义时间的格式
    # Y year年, m month月, d day日, H hour 小时, M minute分, S second秒


    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    #
    suite = unittest.defaultTestLoader.discover('./scripts', 'test*.py')

    # suite=unittest.TestSuite()
    #
    # suite.addTest(scripts.test_login("test_allnotes"))


    # unittest.TextTestRunner() 文本测试用运行器
    # 现在用html的测试用例运行器
    # html的测试用例运行器最终会生成一个html格式的测试报告
    # 我们是不是至少要指定测试报告的路径啊
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path, 'wb')
    HTMLTestRunner(file, 1, "测试报告", "测试环境:Window Server 2008 + Chrome").run(suite)
    file.close()
    # 我们要把html报告作为邮件正文, 发邮件
    send_mail(path)








