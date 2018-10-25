import unittest
from page.LoginPage import caixin_login
from page import LoginPage

class caixinLogin(unittest.TestCase):
    def setUp(self):
        recipe_list=[u"",u""]
        self.mobile=recipe_list[-1]

    def test_caixinLogin(self):
        '''测试登录手机密码正常登录'''
        LoginPage.caixin_login.login(self)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

