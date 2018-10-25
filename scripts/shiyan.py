from appium import webdriver
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
class Ballnotes(unittest.TestCase):
    def setUp(self):
        desired_caps={
        'platformName':'Android',
        'deviceName': 'vivo X20A',
        'platformVersion': '7.1.1',
        'appPackage':'com.caing.news',
        'appActivity':'com.caing.news.activity.LoadingActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
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
        time.sleep(5)

        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id("com.caing.news:id/iv_tegong")
        action1.long_press(el).wait(10000).perform()
        # self.wd.tap([(1020,1040)], 500)
        # TouchAction(self.driver).press(self,el=None,x=1020, y=1040)
        x = int(1020)
        y = int(1040)
        self.driver.swipe(x, y, x, y, 1)

        driver.find_element(By.ID, 'com.caing.news:id/item_log_select_textview').click()
        driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"准生产环境\"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//android.widget.Button[@resource-id=\"android:id/button1\"]').click()
        time.sleep(2)
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
        time.sleep(5)

    def test_alla(self):
        driver=self.driver
        time.sleep(2)
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]").click()

        time.sleep(2)
        driver.find_element(By.ID, "com.caing.news:id/iv_font").click()
        driver.swipe(940, 300, 940, 300, 1)

    def tearDown(self):
        pass
# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()














