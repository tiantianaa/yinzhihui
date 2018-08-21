#coding=utf-8
from appium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from tests.publica.exit_app import *

class Ballnotes(unittest.TestCase):
    def setUp(self):
        desired_caps={
        'platformName':'Android',
        'platformVersion':'4.4.2',
        'deviceName':'127.0.0.1:22515',
        'appPackage':'com.caing.news',
        'appActivity':'com.caing.news.activity.LoadingActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }


        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_allnotes(self):
        driver=self.driver
        time.sleep(15)
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()

        #driver.find_element(By.ID,'com.caing.news:id/loading_layout_ad_close').click()
        # driver.find_element(By.XPATH, "//android.widget.RelativeLayout[@resource-id=\"com.caing.news:id/user_center_setting_top_arrows\"]/android.widget.ImageView[1]").click()
        # driver.find_element(By.ID, 'com.caing.news: id / tv_register').click()

    def test_bllnotes(self):
        driver=self.driver
        time.sleep(15)
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()

    def tearDown(self):
        exitApp(self)
if __name__=='__main__':
    unittest.main()

