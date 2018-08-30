#coding=utf-8
from appium import webdriver
import time
import xlrd
import unittest
from selenium.webdriver.common.by import By
from scripts.publica.exit_app import *

class Ballnotes(unittest.TestCase):
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
        '''最新-全部函数'''
        driver = self.driver
        time.sleep(5)
        # 截图 一
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\picture\\pic1.png")
        # 点击全部
        driver.find_element(By.ID, 'com.youdao.note:id/doc_all').click()
        time.sleep(2)
        # 截图 二
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\picture\\pic2.png")
        # 点击最新
        driver.find_element(By.ID, "com.youdao.note:id/doc_news").click()
        # 截图 三
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\picture\\pic1.png")
    def tearDown(self):
        exitApp(self)
# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()



