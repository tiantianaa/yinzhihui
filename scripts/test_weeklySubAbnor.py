import unittest
from page import WeeklySubAbourPage


class caixinLogin(unittest.TestCase):
    def setUp(self):
        recipe_list=[u"",u""]
        self.mobile=recipe_list[-1]
    def test_weeklyNoLogin(self):
        '''周刊通订阅异常测试，用户没有登录财新账号'''
        WeeklySubAbourPage.weeklySubscribe.weeklyNoLogin(self)
    def test_weeklyLoginWX(self):
        '''周刊通订阅异常测试，用户没有登录微信'''
        WeeklySubAbourPage.weeklySubscribe.weeklyLoginWX(self)
    def test_weeklyLoginZFB(self):
        '''周刊通订阅异常测试，用户未登录支付宝'''
        WeeklySubAbourPage.weeklySubscribe.weeklyLoginZFB(self)
    def test_weeklyAmountLess(self):
        '''订阅异常测试，账户金额不足'''
        WeeklySubAbourPage.weeklySubscribe.weeklyAmountLess(self)
    def test_weeklyPasswordError(self):
        '''周刊通订阅异常测试，交易密码错误'''
        WeeklySubAbourPage.weeklySubscribe.weeklyPasswordError(self)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
