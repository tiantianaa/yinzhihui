import smtplib
import unittest
import os
from email.header import Header
from email.mime.text import MIMEText
import TestCase
from lib.HTMLTestRunner import HTMLTestRunner
import importlib, sys
importlib.reload(sys)
def send_mail(path):
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()
    # MIME multipurse多用途 Internet 互联网  Mail邮件  Extension 扩展
    # MIME是对邮件协议的一个扩展, 使 邮件不仅支持文本,还支持多种格式, 比如图片,音频, 二进制文件等
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = '17600186196@163.com'
    msg['To'] = '17600186196@163.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login('17600186196@163.com', 'abc123456')
    smtp.sendmail('17600186196@163.com', '17600186196@163.com', msg.as_string())
    smtp.quit()
    print('邮件已发送!')

if __name__ == '__main__':
    #now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./TestCase', 'Test*.py')
    base_path = os.path.dirname(__file__)
    #path = base_path + "/report/report" + now + ".html"
    path = base_path + "/reports/report" + ".html"
    file = open(path, 'wb')
    HTMLTestRunner(file, 1, "测试报告", "测试环境:appium Server").run(suite)
    file.close()
    send_mail(path)









