import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time,os

class Base:
    driver=None
    desired_caps = {
        'platformName': 'Android',
        # 'platformVersion': '4.4.4',
        # 'deviceName': '192.168.56.102:5555',
        'deviceName': 'vivo X20A',
        'platformVersion': '7.1.1',
        'appPackage': 'com.caing.news',
        'appActivity': 'com.caing.news.activity.LoadingActivity',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True'
    }

    def __init__(self,appium_driver):
        self.driver=appium_driver

    # def find_element(self,loc):
    #     self.driver.find_element_by_id(*loc).click()

    def findclick(self,loc):
        try:
            #self.driver.find_element(*loc).click()
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).click())
            return self.driver.find_element(*loc).click()
        except:
            return
            #print(u"%s页面中未找到元素" %(self,loc))

    def findtext(self, loc, text):
        try:
            # self.driver.find_element(*loc).click()
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).send_keys(text))
            return self.driver.find_element(*loc).send_keys(text)
        except:
            return

    def find(self, *loc):
        try:
            # self.driver.find_element(*loc).click()
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc))
            return self.driver.find_element(*loc)
        except:
            return

    def findclear(self,loc):
        try:
            #self.driver.find_element(*loc).click()
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).clear())
            return self.driver.find_element(*loc).clear()
        except:
            return

    def findText(self, loc):
        try:
            # self.driver.find_element(*loc).text
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).clear())
            return self.driver.find_element(*loc).text
        except:
            return






