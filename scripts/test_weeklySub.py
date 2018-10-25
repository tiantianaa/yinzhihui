import unittest
from page import WeeklySubPage


class caixinLogin(unittest.TestCase):
    def setUp(self):
        recipe_list=[u"",u""]
        self.mobile=recipe_list[-1]

    def test_caixinLogin(self):
        '''周刊通正常订阅'''
        WeeklySubPage.caixin_login.login(self)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
