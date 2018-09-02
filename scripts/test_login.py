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
        'platformVersion':'4.4.4',
        'deviceName':'192.168.56.102:5555',
        'appPackage':'com.caing.news',
        'appActivity':'com.caing.news.activity.LoadingActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }


        #2.启动appium
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        driver = self.driver

        time.sleep(4)
        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(3)
        for i in range(4):
            print("%d滑屏" % i)
            time.sleep(3)
            driver.swipe(450, 230, 20, 230, 200)
        time.sleep(5)
        driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(5)
        driver.find_element_by_class_name('android.widget.ImageView').click()

    def test_allnotes(self):
        driver=self.driver
        time.sleep(15)
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()

        #driver.find_element(By.ID,'com.caing.news:id/loading_layout_ad_close').click()
        # driver.find_element(By.XPATH, "//android.widget.RelativeLayout[@resource-id=\"com.caing.news:id/user_center_setting_top_arrows\"]/android.widget.ImageView[1]").click()
        # driver.find_element(By.ID, 'com.caing.news: id / tv_register').click()





    def tearDown(self):
        # exitApp(self)
        driver = self.driver
        driver.quit()


# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()

