import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import page.BasePage

class caixin_login(page.BasePage.Base):
    HomeView = (By.XPATH, "//android.widget.ImageView[@resource-id=\"com.caing.news:id/iv_guide_1\"]")
    start = (By.XPATH, "//android.widget.ImageView[@resource-id =\"com.caing.news:id/iv_guide_5\"]")
    close = (By.ID, "com.caing.news:id/iv_finished")
    myself = (By.ID, "com.caing.news:id/iv_myself")
    phoneButton = (By.ID, "com.caing.news:id/user_center_setting_top_phone")

    usernameSend = (By.ID, "com.caing.news:id/user_login_layout_phone")
    passwordSend = (By.ID, "com.caing.news:id/user_login_layout_password")
    loginButton = (By.CLASS_NAME, "android.widget.Button")

    def click_HomeView(self):
        self.find(self.HomeView)
    def click_HomeViewb(self):
        self.findclick(self.start)
    def click_HomeViewc(self):
        self.findclick(self.close)
    def click_myself(self):
        self.findclick(self.myself)
    def click_phoneButton(self):
        self.findclick(self.phoneButton)
    def click_usernameSend(self, text="17600186196"):
        self.findtext(self.usernameSend, text)
    def click_passwordSend(self, text="abc123456"):
        self.findtext(self.passwordSend, text)
    def click_loginButton(self):
        self.findclick(self.loginButton)

    def login(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page=caixin_login(driver)
        time.sleep(2)
        dase_page.click_HomeView()
        time.sleep(2)
        for i in range(4):
            time.sleep(2)
            driver.swipe(450, 230, 20, 230, 200)
        time.sleep(2)
        dase_page.click_HomeViewb()
        time.sleep(2)
        dase_page.click_HomeViewc()
        time.sleep(5)
        action1 = TouchAction(driver)
        el = driver.find_element_by_id('com.caing.news:id/iv_tegong')
        action1.long_press(el).wait(10000).perform()
        # self.wd.tap([(1020,1040)], 500)
        # TouchAction(self.driver).press(self,el=None,x=1020, y=1040)
        driver.swipe(1020, 1040, 1020, 1040, 1)
        time.sleep(3)
        driver.find_element(By.ID, 'com.caing.news:id/item_log_select_textview').click()
        driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"准生产环境\"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//android.widget.Button[@resource-id=\"android:id/button1\"]').click()
        time.sleep(2)
        dase_page.click_HomeView()
        time.sleep(2)
        for i in range(4):
            time.sleep(2)
            driver.swipe(450, 230, 20, 230, 200)
        time.sleep(2)
        dase_page.click_HomeViewb()
        time.sleep(2)
        dase_page.click_HomeViewc()
        # time.sleep(5)
        dase_page.click_myself()
        dase_page.click_phoneButton()
        driver.swipe(450, 1300, 450, 1300, 1)
        time.sleep(2)
        moble = "17600186196"
        dase_page.click_usernameSend(moble)
        time.sleep(8)
        password = "abc123456"
        dase_page.click_passwordSend(password)
        time.sleep(2)
        dase_page.click_loginButton()

































