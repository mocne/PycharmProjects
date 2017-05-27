# -*- coding: utf-8 -*-
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
        sys.setdefaultencoding(u'utf8')
        options = webdriver.ChromeOptions()
        options.add_experimental_option(u'excludeSwitches', [u'ignore-certificate-errors'])
        global browser
        browser = webdriver.Chrome(chrome_options=options)
        # browser.maximize_window()
        browser.implicitly_wait(50.0)
        global isPhoneAuth
        isPhoneAuth = u''
        global isRealName
        isRealName = u''

    def autoBidTest(self):
        print(u'---->: 开始自动投标自动化测试')
        if self.logInCNAiDai() == u'success':
            if self.check_user_info_authentication_state():
                autoState = self.checkAutoState()
                time.sleep(2)
                browser.find_element_by_id('openAutoTender').click()
                time.sleep(1)
                if autoState == u'open':
                    self.close_Automatic_Bid()
                    self.open_Automatic_Bid()
                    self.modify_Automatic_Bid()
                elif autoState == u'close':
                    self.open_Automatic_Bid()
                    self.modify_Automatic_Bid()
                    self.close_Automatic_Bid()
                elif autoState == u'unknown':
                    print(u'---->: 无法获取用户是否开启自动投标')

    def logInCNAiDai(s):
        browser.get(u'http://www.cnaidai.com/webpc/index.html')
        time.sleep(2)
        print(u'---->: 打开老平台登录网址')
        time.sleep(2)
        browser.find_element_by_xpath(u'/html/body/div[11]/div').click()
        time.sleep(2)
        browser.find_element_by_xpath(u'/html/body/div[2]/div/ul/li[4]/a').click()
        print (u'---->: 关闭广告宣传弹窗\n---->: 进入老版爱贷登录页……')
        # stepNum += 1
        time.sleep(1)

        # 开始输入用户名和密码以及验证码
        print(u'---->: 开始输入用户信息进行登录……')
        time.sleep(1)
        usernameLabel = browser.find_element_by_name(u'username')
        usernameLabel.clear()
        usernameLabel.send_keys(Keys.F11, u'wz001')
        print(u'---->: 输入用户名……')
        time.sleep(1)
        passwordLabel = browser.find_element_by_name(u'password')
        passwordLabel.clear()
        passwordLabel.send_keys(u'a1111111')
        print(u'---->: 输入密码……')
        time.sleep(1)
        valicodeLabel = browser.find_element_by_name(u'valicode')
        valicodeLabel.clear()
        valicodeLabel.send_keys(u'1111')
        time.sleep(1)
        print(u'---->: 输入验证码……')
        time.sleep(1)
        browser.find_element_by_id(u'login_submit').click()
        time.sleep(1)
        # if browser.find_element_by_class_name(u'login_msg'):
        #     print(u'\n##################\n\n---->: 系统异常，请稍后使用……\n\n##################')
        #     return
        print(u'---->: 开始登录老平台……')
        time.sleep(5)
        browser.refresh()
        return u'success'

    def check_user_state(self):
        print(u'---->: 开始验证用户状态……')

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
        print (u'---->: 开始检查自动投标状态……')
        time.sleep(5)
        autoBtnText = browser.find_element_by_id(u'openAutoTender').text
        if autoBtnText == u'已开启 >':
            print(u'---->: 自动投标已开启')
            autoState_check = u'open'
        elif autoBtnText == u'未开启 >':
            print(u'---->: 自动投标未开启')
            autoState_check = u'close'
        else:
            print(u'---->: 不能获取是否开启自动投标')
            autoState_check = u'unknown'
        return autoState_check

    def open_Automatic_Bid(self):
        print('---->: 开始开启自动投标\n---->: 点击switch开关(open)')
        browser.refresh()
        time.sleep(2)
        # browser.find_element_by_id('openAutoTender').click()
        time.sleep(1)
        browser.find_element_by_class_name('close1').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(2)
        print(u'开启-自动投标-已结束')

    def modify_Automatic_Bid(self):
        browser.refresh()
        time.sleep(1)
        browser.find_element_by_class_name(u'revise-btn').click()
        print(u'---->: 进入修改页面')
        time.sleep(2)
        print(u'---->: 选取年化率')
        selMin = browser.find_element_by_id(u'minimumProfit')
        selMax = browser.find_element_by_id(u'maximumProfit')
        numMin = random.randint(1, 24)
        numMax = random.randint(1, 24)
        while (numMin > numMax) :
            numMax = random.randint(1, 24)
        print '---->: 最小是: ', numMin, '    最大是: ', numMax
        time.sleep(1)
        Select(selMin).select_by_index(numMin - 1)
        time.sleep(1)
        Select(selMax).select_by_index(numMax - 1)
        time.sleep(1)
        for i in range(0, 5):
            dateIndex = random.randint(1, 5)
            print u'dateIndex: ', dateIndex
            one_month = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(1)')
            three_month = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(2)')
            six_month = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(3)')
            twelve_month = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(4)')
            eighteen_month = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(5)')

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
                print('someOne is selected')
            else:
                six_month.click()
                time.sleep(1)
                twelve_month.click()
                time.sleep(1)
        print '#########################################################################'
        total = 10000
        li = [i for i in range(total)]
        res = []
        for i in range(2):
            t = random.randint(i, total - 1)
            res.append(li[t])
        print res, res[0], res[1]
        print '###########################################################################'
        minAmount = res[0]
        maxAmount = res[1]
        if minAmount > maxAmount:
            maxAmount, minAmount = minAmount, maxAmount
        print('---->: 最小金额是: ', minAmount, '    最大金额是: ', maxAmount)
        time.sleep(3)
        minAmount = browser.find_element_by_id('minimumAmount')
        minAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        minAmount.send_keys(Keys.DELETE)
        minAmount.send_keys(res[0]*100)
        time.sleep(2)
        maxAmount = browser.find_element_by_id('maximumAmount')
        maxAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        maxAmount.send_keys(Keys.DELETE)
        maxAmount.send_keys(res[1]*100)
        time.sleep(2)

        discount_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(1)')
        interest_add_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(2)')

        ticketIndex = random.randint(1, 3)
        print('---->: 优惠券选取：', ticketIndex, '<1：加息券；2：折扣券：3：全部选择>')
        time.sleep(3)
        if ticketIndex == 1:
            discount_ticket.click()
            time.sleep(2)
        elif ticketIndex == 2:
            interest_add_ticket.click()
            time.sleep(2)
        else:
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
        print('修改-自动投标-结束')

    def close_Automatic_Bid(self):
        print(u'---->: 开始关闭自动投标\n---->: 点击switch按钮(close)')
        time.sleep(2)
        # browser.find_element_by_id('openAutoTender').click()
        time.sleep(1)
        browser.find_element_by_class_name(u'open1').click()
        time.sleep(1)
        browser.find_element_by_id(u'payPassWord').send_keys(u'111111')
        time.sleep(2)
        browser.find_element_by_xpath(u'/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(2)
        print(u'关闭-自动投标-结束')

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