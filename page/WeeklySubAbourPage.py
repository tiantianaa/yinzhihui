import time
from appium import webdriver
from selenium.webdriver.common.by import By
import page.BasePage
from appium.webdriver.common.touch_action import TouchAction

class weeklySubscribe(page.BasePage.Base):
    HomeView = (By.XPATH, "//android.widget.ImageView[@resource-id=\"com.caing.news:id/iv_guide_1\"]")
    start = (By.XPATH, "//android.widget.ImageView[@resource-id =\"com.caing.news:id/iv_guide_5\"]")
    close = (By.ID, "com.caing.news:id/iv_finished")

    myself = (By.ID, "com.caing.news:id/iv_myself")
    phoneButton = (By.ID, "com.caing.news:id/user_center_setting_top_phone")

    usernameSend = (By.ID, "com.caing.news:id/user_login_layout_phone")
    passwordSend = (By.ID, "com.caing.news:id/user_login_layout_password")
    loginButton = (By.CLASS_NAME, "android.widget.Button")

    # 订阅周刊通
    # newsButton = (By.ID, "com.caing.news:id/iv_summary")
    #
    # chooseArticle = (By.XPATH,"//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
    chooseCategory = (By.ID, "com.caing.news:id/cb_check")
    nowSubscribe = (By.ID, "com.caing.news:id/tv_subscribe")
    zfbpay = (By.XPATH,
              "//android.support.v7.widget.RecyclerView[@resource-id=\"com.caing.news:id/pay_method_recyclerview\"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]")
    weixinpay=(By.XPATH,"//android.support.v7.widget.RecyclerView[@resource-id=\"com.caing.news:id/pay_method_recyclerview\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    Pay = (By.ID, "com.caing.news:id/tv_pay")


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

    def click_chooseCategory(self):
        self.findclick(self.chooseCategory)

    def click_nowSubscribe(self):
        self.findclick(self.nowSubscribe)

    def click_zfbpay(self):
        self.findclick(self.zfbpay)
    def click_weixinpay(self):
        self.findclick(self.weixinpay)
    def click_Pay(self):
        self.findclick(self.Pay)

        # 订阅周刊通

    # def click_newsButton(self):
    #     self.findclick(self.newsButton)
    # def click_chooseArticle(self):
    #     self.findclick(self.chooseArticle)

    def weeklyNoLogin(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page = weeklySubscribe(driver)
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
        time.sleep(3)

        # 订阅周刊通
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        driver.find_element(By.XPATH,
                            '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(5)
        for i in range(3):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(300, 350, 300, 20, 200)
        # 点击订阅
        driver.find_element(By.XPATH, "//android.view.View/android.view.View[6]/android.view.View[3]").click()

        actual = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@resource-id=\"com.caing.news:id/user_login_layout_login_password_or_captcha\"]").text
        self.assertEqual(actual, u'手机号密码登录')
        driver.quit()

    def weeklyLoginWX(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page = weeklySubscribe(driver)
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

        # 订阅周刊通
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        driver.find_element(By.XPATH,
                            '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(5)
        for i in range(3):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(300, 350, 300, 20, 200)
        # 点击订阅
        driver.find_element(By.XPATH, "//android.view.View/android.view.View[6]/android.view.View[3]").click()

        dase_page.click_chooseCategory()
        dase_page.click_nowSubscribe()
        dase_page.click_weixinpay()
        dase_page.click_Pay()
        time.sleep(3)

        actual = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@resource-id=\"com.caing.news:id/user_login_layout_login_password_or_captcha\"]").text
        self.assertEqual(actual, u'微信号/QQ/邮箱登录')
        driver.quit()

    def weeklyLoginZFB(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page = weeklySubscribe(driver)
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

        # 订阅周刊通
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        driver.find_element(By.XPATH,
                            '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(5)
        for i in range(3):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(300, 350, 300, 20, 200)
        # 点击订阅
        driver.find_element(By.XPATH, "//android.view.View/android.view.View[6]/android.view.View[3]").click()
        dase_page.click_chooseCategory()
        dase_page.click_nowSubscribe()
        dase_page.click_zfbpay()
        dase_page.click_Pay()
        time.sleep(3)
        actual = driver.find_element(By.ID,"com.eg.android.AlipayGphone:id/loginButton").text
        self.assertEqual(actual, u'登录')
        driver.quit()

    def weeklyAmountLess(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page = weeklySubscribe(driver)
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

        # 订阅周刊通
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        driver.find_element(By.XPATH,
                            '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(5)
        for i in range(3):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(300, 350, 300, 20, 200)
        # 点击订阅
        driver.find_element(By.XPATH, "//android.view.View/android.view.View[6]/android.view.View[3]").click()

        dase_page.click_chooseCategory()
        dase_page.click_nowSubscribe()
        dase_page.click_zfbpay()
        dase_page.click_Pay()
        time.sleep(3)
        driver.swipe(80, 1280, 80, 1280, 1)
        driver.swipe(500, 1400, 500, 1400, 1)

        # driver.find_element(By.XPATH,
        #                     "//android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]")
        time.sleep(3)
        driver.swipe(500, 1900, 500, 1900, 1)

        driver.swipe(540, 1700, 540, 1700, 1)
        driver.swipe(540, 1880, 540, 1880, 1)
        driver.swipe(540, 1600, 540, 1600, 1)
        driver.swipe(540, 1700, 540, 1700, 1)
        driver.swipe(540, 1880, 540, 1880, 1)
        driver.swipe(540, 1600, 540, 1600, 1)

        driver.quit()

        # driver.swipe(600, 850, 600, 850, 1)
        # driver.find_element(By.ID, "com.tencent.mm:id/apj").click()

    def weeklyPasswordError(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", page.BasePage.Base.desired_caps)
        dase_page = weeklySubscribe(driver)
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

        # 订阅周刊通
        driver.find_element(By.ID, 'com.caing.news:id/iv_summary').click()
        driver.find_element(By.XPATH,
                            '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(5)
        for i in range(3):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(300, 350, 300, 20, 200)
        # 点击订阅
        driver.find_element(By.XPATH, "//android.view.View/android.view.View[6]/android.view.View[3]").click()

        dase_page.click_chooseCategory()
        dase_page.click_nowSubscribe()
        dase_page.click_zfbpay()
        dase_page.click_Pay()
        time.sleep(3)
        driver.swipe(80, 1280, 80, 1280, 1)
        driver.swipe(500, 1400, 500, 1400, 1)

        # driver.find_element(By.XPATH,
        #                     "//android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]")
        time.sleep(3)
        driver.swipe(500, 1900, 500, 1900, 1)

        driver.swipe(540, 1700, 540, 1700, 1)
        driver.swipe(540, 1700, 540, 1700, 1)
        driver.swipe(540, 1880, 540, 1880, 1)
        driver.swipe(540, 1880, 540, 1880, 1)
        driver.swipe(540, 1600, 540, 1600, 1)
        driver.swipe(540, 1600, 540, 1600, 1)

        driver.quit()




































































