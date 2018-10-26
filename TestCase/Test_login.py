from appium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
class Ballnotes(unittest.TestCase):
    def setUp(self):
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

        # 获取屏幕的size
        size = driver.get_window_size()
        print(size)
        # 获取屏幕宽度 width
        width = size['width']
        print(width)
        # 获取屏幕高度 height
        height = size['height']
        print(height)
       # driver.find_element_by_xpath()


    def test_alla(self):
        driver=self.driver
        time.sleep(8)
        try:
            driver.find_element(By.ID, 'com.caing.news:id/iv_myself').click()
            driver.find_element(By.ID, 'com.caing.news:id/user_center_setting_top_phone').click()
            driver.find_element(By.XPATH,
                                '//android.widget.TextView[@resource-id=\"com.caing.news:id/user_login_layout_login_password_or_captcha\"]').click()
            driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_phone').send_keys("176")
            driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_password').send_keys("abc123456")
            driver.find_element(By.ID, 'com.caing.news:id/user_login_layout_login').click()

            actual = driver.find_element(By.ID, "com.caing.news:id/user_login_layout_phone_error").text
            self.assertEqual(actual, u'请输入正确的手机')
        except Exception as msg:
            driver.get_screenshot_as_file('picture\\image.png')
            raise msg

    def tearDown(self):
        pass

# 当该程序做为主程序时，才会调用后面的代码
if __name__=='__main__':
    unittest.main()
    # aa=Ballnotes.test_alla
    # suite = unittest.TestLoader().loadTestsFromTestCase(Ballnotes)
    # unittest.TextTestRunner(verbosity=2).run(suite)












