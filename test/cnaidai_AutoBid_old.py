# -*- coding: utf-8 -*-
# encoding: utf-8
__author__ = 'pkf'

from selenium import webdriver
import time, datetime, sys, os
import unittest, random
import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests, json

class Automatic_Bid(unittest.TestCase):

    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
        global browser
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(50.0)
        global isPhoneAuth
        isPhoneAuth = ''
        global isRealName
        isRealName = ''
        global isAutoStateOpen
        isAutoStateOpen = ''

    def autoBidTest(self):
        print('---->: 开始自动投标自动化测试')
        if self.logInCNAiDai() == 'success':
            if self.check_user_info_authentication_state():
                autoState = self.checkAutoState()
                time.sleep(2)
                browser.find_element_by_id('openAutoTender').click()
                time.sleep(1)
                if autoState == 'open':
                    self.close_Automatic_Bid()
                    self.open_Automatic_Bid()
                    self.modify_Automatic_Bid()
                    time.sleep(3)
                    browser.quit()
                elif autoState == 'close':
                    self.open_Automatic_Bid()
                    self.modify_Automatic_Bid()
                    self.close_Automatic_Bid()
                    time.sleep(3)
                    browser.quit()
                elif autoState == 'unknown':
                    print('---->: 无法获取用户是否开启自动投标')

    def logInCNAiDai(s):
        browser.get('http://www.cnaidai.com/webpc/index.html')
        time.sleep(2)
        print('---->: 打开老平台登录网址')
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[11]/div').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[4]/a').click()
        print ('---->: 关闭广告宣传弹窗\n---->: 进入老版爱贷登录页……')
        # stepNum += 1
        time.sleep(1)

        # 开始输入用户名和密码以及验证码
        print('---->: 开始输入用户信息进行登录……')
        time.sleep(1)
        usernameLabel = browser.find_element_by_name('username')
        usernameLabel.clear()
        usernameLabel.send_keys(Keys.F11, 'wz001')
        print('---->: 输入用户名……')
        time.sleep(1)
        passwordLabel = browser.find_element_by_name('password')
        passwordLabel.clear()
        passwordLabel.send_keys('a1111111')
        print('---->: 输入密码……')
        time.sleep(1)
        valicodeLabel = browser.find_element_by_name('valicode')
        valicodeLabel.clear()
        valicodeLabel.send_keys('1111')
        print('---->: 输入验证码……')
        time.sleep(1)
        browser.find_element_by_id('login_submit').click()
        time.sleep(1)
        # if browser.find_element_by_class_name(u'login_msg'):
        #     print(u'\n##################\n\n---->: 系统异常，请稍后使用……\n\n##################')
        #     return
        print('---->: 开始登录老平台……')
        time.sleep(5)
        browser.refresh()
        return 'success'

    def check_user_state(self):
        print('---->: 开始验证用户状态……')

    def check_user_info_authentication_state(s):
        print(u'---->: 开始验证用户认证状态……')
        time.sleep(2)
        if browser.find_element_by_class_name(u'credit_pic_card_1'):
            auth_code_P = u'1'
            if browser.find_element_by_class_name(u'credit_pic_phone_1'):
                auth_code_N = u'1'
                print(u'---->: 用户全部认证成功')
                return (u'AllAuth')
            else:
                print(u'---->: 已实名认证，未手机认证')
                return (u'NameAuth')
        else:
            if browser.find_element_by_class_name(u'credit_pic_phone_1'):
                auth_code_N = u'1'
                print(u'---->: 未实名认证，已手机认证')
                return (u'PhoneAuth')
            else:
                print(u'---->: 没有进行手机认证')
                return (u'NoneAuth')
        time.sleep(2)

    def checkAutoState(autoState_check):
        print ('---->: 开始检查自动投标状态……')
        time.sleep(5)
        autoBtnText = browser.find_element_by_id('openAutoTender').text
        if autoBtnText == '已开启 >':
            print('---->: 自动投标已开启')
            autoState_check = 'open'
        elif autoBtnText == '未开启 >':
            print('---->: 自动投标未开启')
            autoState_check = 'close'
        else:
            print('---->: 不能获取是否开启自动投标')
            autoState_check = 'unknown'
        return autoState_check

    def open_Automatic_Bid(self):
        print('---->: 开始开启自动投标\n---->: 点击switch开关(open)')
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_class_name('close1').click()
        time.sleep(1)
        print('---->: 输入交易密码')
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        print('---->: 点击确认')
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(2)
        print('---->: 开启-自动投标-已结束')

    def modify_Automatic_Bid(self):
        browser.refresh()
        time.sleep(1)
        browser.find_element_by_class_name('revise-btn').click()
        print('---->: 进入修改页面')
        time.sleep(2)
        print('---->: 选取年化率')
        selMin = browser.find_element_by_id('minimumProfit')
        selMax = browser.find_element_by_id('maximumProfit')
        numMin = random.randint(1, 24)
        numMax = random.randint(1, 24)
        if numMin > numMax:
            numMin, numMax = numMax, numMin
        print('---->: min:', numMin, '---max:', numMax)
        time.sleep(1)
        print('---->: 选取最小值')
        Select(selMin).select_by_index(numMin - 1)
        time.sleep(1)
        print('---->: 选取最大值')
        Select(selMax).select_by_index(numMax - 1)
        time.sleep(1)

        for i in range(0, 5):
            dateIndex = random.randint(1, 5)
            print '---->: 选取第 ', dateIndex, '个日期选框 '
            one_month = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(1)')
            three_month = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(2)')
            six_month = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(3)')
            twelve_month = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(4)')
            eighteen_month = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(5)')

            if dateIndex == 1:
                one_month.click()
                time.sleep(1)
            elif dateIndex == 2:
                three_month.click()
                time.sleep(1)
            elif dateIndex == 3:
                six_month.click()
                time.sleep(1)
            elif dateIndex == 4:
                twelve_month.click()
                time.sleep(1)
            else:
                eighteen_month.click()
                time.sleep(1)
            if one_month.is_selected() or three_month.is_selected() or six_month.is_selected() or twelve_month.is_selected() or eighteen_month.is_selected():
                print('---->: 有至少一个被选中')
            else:
                print('---->: 选取第 3 个日期选框')
                six_month.click()
                time.sleep(1)
                print('---->: 选取第 4 个日期选框')
                twelve_month.click()
                time.sleep(1)

        total = 10000
        li = [i for i in range(total)]
        res = random.sample(li, 2)
        if (res[0] > res[1]):
            res[0], res[1] = res[1], res[0]
        minAmount = res[0]
        maxAmount = res[1]
        time.sleep(3)
        print('---->: 输入单笔投资金额最小值')
        minAmount = browser.find_element_by_id('minimumAmount')
        minAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        minAmount.send_keys(Keys.DELETE)
        minAmount.send_keys(res[0]*100)
        time.sleep(2)
        print('---->: 输入单笔投资金额最大值')
        maxAmount = browser.find_element_by_id('maximumAmount')
        maxAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        maxAmount.send_keys(Keys.DELETE)
        maxAmount.send_keys(res[1]*100)
        time.sleep(2)

        discount_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(1)')
        interest_add_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(2)')
        ticketIndex = random.randint(1, 3)
        time.sleep(3)
        if ticketIndex == 1:
            print('---->: 点击-加息券')
            discount_ticket.click()
            time.sleep(2)
        elif ticketIndex == 2:
            print('---->: 点击-折扣券')
            interest_add_ticket.click()
            time.sleep(2)
        else:
            print('---->: 点击-加息券和折扣券')
            discount_ticket.click()
            time.sleep(2)
            interest_add_ticket.click()
            time.sleep(2)

        print('---->: 点击设置并保存按钮')
        browser.find_element_by_class_name('btn-save').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        browser.find_element_by_class_name('btn-ensure').click()
        time.sleep(1)
        print('---->: 修改-自动投标-结束')

    def close_Automatic_Bid(self):
        print('---->: 开始关闭自动投标\n---->: 点击switch按钮(close)')
        time.sleep(2)
        # browser.find_element_by_id('openAutoTender').click()
        time.sleep(1)
        browser.find_element_by_class_name('open1').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys(u'111111')
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(2)
        print('---->: 关闭-自动投标-结束')

    def get_ScreenShot(self):
        now = time.strftime(u'%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = u'..\\result\\image\\' + now + u'.png'
        print pic_path
        browser.save_screenshot(pic_path)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid('autoBidTest'))

    runner = unittest.TextTestRunner()
    runner.run(suite)