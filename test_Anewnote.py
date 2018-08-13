#coding=utf-8
import unittest
from appium import webdriver
import time
from selenium.webdriver.common.by import By

import xlrd
from .public.exit_app import *



class Anewnote(unittest.TestCase):
    '''新建云笔记'''
    #'''三引号可以在报告中加入中文注释
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            'platformVersion':'4.4.4',
            'deviceName':'192.168.56.101:5555',
            'appPackage':'com.youdao.note',
            'appActiviy':'.activity2.SplashActivity',
            'unicodeKeyboard':'True',#防止中文不能输入
            'resetKeyboard':'True'# 重置设置生效
        }
        self.driver=webdriver.Remote('http:127.0.0.1:4723/wd/hub',desired_caps)
    def test_newnote(self):
        driver=self.driver
        time.sleep(4)
        #引入参数文件路径
        wd=xlrd.open_workbook("C:\\Users\\Administrator\\PycharmProjects\\untitled11111111111\\data\\data.xls")
        sh=wd.sheet_by_name('note')
        r_num=sh.nrows
        for i in range(1,r_num):
            title=sh.cell_value(i,1)
            content=sh.cell_value(i,2)
            expect=sh.cell_value(i,3)
            # +
            driver.find_element(By.ID,'com.youdao.note:id/add_note_floater_open').click()
            #新建笔记

            driver.find_element(By.NAME,'新建笔记').click()
            #标题
            driver.find_element(By.ID,'com.youdao.note:id/note_title').send_keys(title)
            #内容
            driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\'com.youdao.note:id/note_content\']/android.widget.EditText[1]').send_keys(content)
            #完成
            driver.find_element(By.ID,'com.youdao.note:id/actionbar_complete_text').click()
    def tearDown(self):
        #退出app
        exitApp(self)




