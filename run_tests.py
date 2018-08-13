#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
按住Ctrl 点击sys，将以下两行代码复制到sys.py文件的末尾
def setdefaultencoding(param):
    return None
'''

def getSuite():
    #1>获取脚本的存放位置
    test_dir='C:\\Users\\Administrator\\PycharmProjects\\AppTest\\scripts'
    #2>获取要运行的脚本，并将其加入测试集
    #discover(参数1,参数2)
    #参数1：脚本的存放位置
    #参数2：脚本格式pattern 以test开头，以.py结尾的文件，test*.pyun
    discov=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #3>将我们要运行（获取）的脚本加入到测试集中
    suite=unittest.TestSuite(discov)
    #遍历循环
    for testcase in discov:
         suite.addTest(testcase)
    #返回到测试集中
    return suite

#报告的设计
def designReport():
    global runner
    global file_rt
    global report_name
    #把HTMLTestRunner.py文件放入 Lib目录下
    now=time.strftime('%Y-%m-%d %H-%M-%S')
    #表示当前的目录
    report_name=".\\report\\"+now+"result.html"
    file_rt=open(report_name,'wb')
    runner=HTMLTestRunner(stream=file_rt,title='appium_youdao_test',description='测试结果')
#发送邮件
def sendEmail(rt):
    f=open(rt,'rb')#rb二进制的读取方式--打开
    mail_body=f.read() #将报告作为正文
    msg=MIMEText(mail_body,'html','utf-8')#给邮件规定格式
    msg['Subject']=Header('appium 测试报告','utf-8')#主题
    msg['From']='17600186196@163.com'#发件人
    msg['To']='17600186196@163.com'
    smtp=smtplib.SMTP('smtp.163.com')
    smtp.login('17600186196@163.com','ctt741211358')#邮箱的用户名和密码
    smtp.quit()#执行结束后，退出
    print('------邮件发送成功-------')
#调用（运行）驱动
suites=getSuite()
designReport()
runner.run(suites)
file_rt.close()
sendEmail(report_name)
#退出app
def exitApp(self):
    driver=self.driver
    driver.quit()
