from appium import webdriver
import time
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
        'deviceName':'127.0.0.1:22515',
        'appPackage':'com.caing.news',
        'appActivity':'com.caing.news.activity.LoadingActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }


        #2.启动appium
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_allnotes(self):
        '''最新-全部函数'''
        driver=self.driver
        time.sleep(5)
        #
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()
        # driver.find_element(By.XPATH, "//android.widget.RelativeLayout[@resource-id=\"com.caing.news:id/user_center_setting_top_arrows\"]/android.widget.ImageView[1]").click()
        # driver.find_element(By.ID, 'com.caing.news: id / tv_register').click()




    def tearDown(self):
        exitApp(self)
# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()

