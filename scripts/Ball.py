#coding=utf-8
from appium import webdriver
import time
import xlrd
import unittest
from selenium.webdriver.common.by import By
from scripts.publica.exit_app import *

class ball(unittest.TestCase):
    '''最新-全部切换'''
    def setUp(self):
        #1.手机信息
        desired_caps={
        'platformName':'Android',
        'platformVersion':'4.4.2',
        'deviceName':'192.168.56.101:5555',
        'appPackage':'com.youdao.note',
        'appActivity':'com.youdao.note.activity2.SplashActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }
        #2.启动appium
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_allnotes(self):
        u"""百度搜索"""
        driver = self.driver
        time.sleep(5)
        driver.find_element(By.ID, 'com.youdao.note:id/doc_all').click()
    def test_allnote(self):
        u'''新-全部函数'''
        driver = self.driver
        time.sleep(5)
        driver.find_element(By.ID, "com.youdao.note:id/doc_news").click()
    def tearDown(self):
        exitApp(self)
# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()



