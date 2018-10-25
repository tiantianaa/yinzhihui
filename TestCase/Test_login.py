from appium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from scripts.publica.exit_app import *
import ddt
@ddt.ddt
class Ballnotes(unittest.TestCase):
    '''最新登录滑屏'''

    def setUp(self):
        #1.手机信息
        desired_caps={
        'platformName':'Android',
        # 'platformVersion': '4.4.4',
        # 'deviceName':'192.168.56.102:5555',
        'deviceName': 'vivo X20A',
        'platformVersion': '7.1.1',
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
            time.sleep(3)
            driver.swipe(450, 230, 20, 230, 200)
        time.sleep(5)
        driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(5)
        driver.find_element_by_class_name('android.widget.ImageView').click()
       # driver.find_element_by_xpath()





    def test_alla(self):
        '''最新登录滑屏AAAAA'''
        driver=self.driver
        time.sleep(8)
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()
        driver.find_element(By.ID, 'com.caing.news:id/user_center_setting_top_phone').click()
        driver.find_element(By.XPATH,
                            '//android.widget.TextView[@resource-id=\"com.caing.news:id/user_login_layout_login_password_or_captcha\"]').click()
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_phone').send_keys("176")
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_password').send_keys("abc123456")
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_login').click()

        actual = driver.find_element(By.ID, "com.caing.news:id/user_login_layout_phone_error").text
        self.assertEqual(actual, u'请输入正确的手机号')
        print("ok")

        driver.find_element(By.ID,'com.caing.news:id/user_login_layout_left_icon').click()






    def test_allb(self):
        '''最新登录滑屏BBBBB'''
        driver = self.driver
        time.sleep(8)
        driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()
        driver.find_element(By.ID, 'com.caing.news:id/user_center_setting_top_phone').click()
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"com.caing.news:id/user_login_layout_login_password_or_captcha\"]').click()
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_phone').send_keys("17600186196")
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_password').send_keys("abc")
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_login').click()

        actual = driver.find_element(By.ID, "com.caing.news:id/user_login_layout_password_error").text
        self.assertEqual(actual, u'请输入正确格式的密码')
        driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_left_icon').click()
    # def test_allc(self):
    #     '''最新登录滑屏CCCCC'''
    #     driver = self.driver
    #     time.sleep(15)
    #     driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()
    #     print("第三个")
        print("ok")



    def tearDown(self):
        exitApp(self)
# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()

'''
不加装饰器@classMethod的情况下，不是数据驱动测试的时候，测试用例是分开执行的  这个可以拿来用
加装饰器@classMethod的情况下，不是数据驱动测试的时候，测试受到了影响不可行 不能用
加上装饰器@classMethod的情况下，是驱动测试，ddt装饰器情况下,受影响了不可用  
不加装饰器@classMethod的情况下，是驱动测试，ddt装饰器情况下，不是for循环 这个可以拿来用
不加装饰器@classMethod的情况下，是驱动测试，无ddt装饰器情况下，不成立，一个失败都失败了

'''












