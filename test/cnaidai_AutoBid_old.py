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
        sys.setdefaultencoding('utf8')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
        global browser
        browser = webdriver.Chrome(chrome_options=options)
        # browser.maximize_window()
        browser.implicitly_wait(50.0)
        global isPhoneAuth
        isPhoneAuth = ''
        global isRealName
        isRealName = ''

    def logInCnaidai(self):
        browser.get('http://www.cnaidai.com/webpc/index.html')
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[11]/div').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[4]/a').click()
        print ('---->: Close_alert_View\n---->: Come_to_Cnaidai_Old_loginPage')
        # stepNum += 1
        time.sleep(1)

        # 开始输入用户名和密码以及验证码
        print('---->: Start to input userMessage')
        usernameLabel = browser.find_element_by_name('username')
        usernameLabel.clear()
        usernameLabel.send_keys(Keys.F11, 'wz001')
        print('---->: 输入用户名……')
        passwordLabel = browser.find_element_by_name('password')
        passwordLabel.clear()
        passwordLabel.send_keys('a1111111')
        print('---->: 输入密码……')
        valicodeLabel = browser.find_element_by_name('valicode')
        valicodeLabel.clear()
        valicodeLabel.send_keys('1111')
        print('---->: 输入验证码……')
        time.sleep(1)
        browser.find_element_by_id('login_submit').click()
        print('---->: 开始登录老平台……')
        time.sleep(5)
        browser.refresh()
        time.sleep(1)
        self.check_user_info_authentication_state()
        time.sleep(1)
        # global autoState
        # autoState = self.checkAutoState()
        # print(autoState)

    def check_user_state(self):
        print('---->: 开始验证用户状态……')

    def check_user_info_authentication_state(self):
        print('---->: 开始验证用户认证状态……')
        session = requests.session()
        loginURl = 'http://a.cnaidai.com/webjr/uc/indexCfg/account/userInfo.cgi?'
        uTime = int(time.mktime(datetime.datetime.now().timetuple()) * 1000)
        loginData = {'_': uTime}
        userInfo = session.post(loginURl, data=loginData, headers=self.headers)
        print(userInfo)
        dic_json = json.dumps(userInfo.json(), sort_keys=True, indent=10, ensure_ascii=False)
        dicInfo = json.loads(dic_json)
        print('---->: Response : ', dicInfo)
        userInfo_detail = int(dicInfo['detailuser'])
        print('---->: 用户详细信息：', userInfo_detail)
        isPhoneAuth = userInfo_detail['phoneStatus']
        if isPhoneAuth == '1':
            print('已验证手机号码')
        else: print('未验证手机号码')
        isRealName = userInfo_detail['realStatus']
        if isRealName == '1':
            print('已实名认证')
        else: print('未实名认证')
        isOpenAutoBid = dicInfo['openAutoTender']
        if isOpenAutoBid == '1':
            print('---->: 已开启自动投标')
        else:print('---->: 未开启自动投标')

        global auth_code
        #auth_code(phone,realName,bankCard)
        auth_code = '000'


    def checkAutoState(autoState_check):
        print ('---->: Start_checkAutoBidState')
        time.sleep(5)
        autoBtnText = browser.find_element_by_id('openAutoTender').text
        print autoBtnText
        if autoBtnText == '已开启 >':
            print('---->: 自动投标已开启')
            autoState_check = '1'
            # print('---->: Start to modify Automatic_Bid')
            # browser.find_element_by_id('openAutoTender').click()
        elif autoBtnText == '未开启 >':
            print('---->: Automatic_Bid is Close')
            autoState_check = '0'
            # print('---->: start to open Automatic_Bid')
            # browser.find_element_by_id('openAutoTender').click()
            # time.sleep(2)
            # self.open_Automatic_Bid()
            # time.sleep(2)
            # print('---->: Start to modify Automatic_Bid')
            # self.modify_Automatic_Bid()
            # time.sleep(2)
            # self.close_Automatic_Bid()
            # time.sleep(2)
        else:
            print('---->: Cant't get the State')
            autoState_check = '5'
        print(autoState_check)
        return autoState_check

    def open_Automatic_Bid(self):
        print('---->: Start to click switch to open')
        browser.refresh()
        time.sleep(1)
        browser.find_element_by_class_name('close1').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(1)
        browser.switch_to_alert().accept()
        time.sleep(2)

    def modify_Automatic_Bid(self):
        browser.refresh()
        time.sleep(1)
        browser.find_element_by_class_name('revise-btn').click()
        print('---->: Come_into_modify_View')
        time.sleep(2)
        print('---->: Start to select minProfit')
        # browser.find_element_by_id('minimumProfit').click()
        # time.sleep(1)
        selMin = browser.find_element_by_id('minimumProfit')
        selMax = browser.find_element_by_id('maximumProfit')
        numMin = random.randint(1,24)
        numMax = random.randint(1,24)
        while (numMin > numMax) :
            numMax = random.randint(1, 24)
        print ('minNum: ',numMin,'    maxNum: ',numMax)
        time.sleep(1)
        Select(selMin).select_by_index(numMin - 1)
        time.sleep(1)
        Select(selMax).select_by_index(numMax - 1)
        time.sleep(1)
        for i in range(0,5):
            dateIndex = random.randint(1,5)
            print ('dateIndex: ',dateIndex)
            if dateIndex == 1:
                browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(1)').click()
                time.sleep(1)
            elif dateIndex == 2:
                browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(2)').click()
                time.sleep(1)
            elif dateIndex == 3:
                browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(3)').click()
                time.sleep(1)
            elif dateIndex == 4:
                browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(4)').click()
                time.sleep(1)
            else:
                browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(5)').click()
                time.sleep(1)
        minAmount = random.randint(1, 10000) * 100
        maxAmount = random.randint(1, 10000) * 100
        while (minAmount > maxAmount):
            maxAmount = random.randint(1, 10000) * 100
        print('minAmount: ', minAmount, 'maxAmount: ', maxAmount)
        time.sleep(3)
        minAmount = browser.find_element_by_id('minimumAmount')
        minAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        minAmount.send_keys(Keys.DELETE)
        minAmount.send_keys(minAmount)
        time.sleep(2)
        maxAmount = browser.find_element_by_id('maximumAmount')
        # minAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        # minAmount.send_keys(Keys.DELETE)
        # maxAmount.send_keys(int(maxAmount * 100))
        time.sleep(2)

        discount_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(1)')
        interest_add_ticket = browser.find_element_by_css_selector('#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(2)')

        ticketIndex = random.randint(1,3)
        print('ticketIndex',ticketIndex)
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

        print('---->: Start to Set_Save')
        browser.find_element_by_class_name('btn-save').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        browser.find_element_by_class_name('btn-ensure').click()
        time.sleep(1)
        browser.switch_to_alert().accept()

    def close_Automatic_Bid(self):
        print('---->: start to close Automatic_Bid\n---->: Start to click switch to close')
        browser.find_element_by_id('openAutoTender').click()
        time.sleep(1)
        browser.find_element_by_class_name('open1').click()
        time.sleep(1)
        browser.find_element_by_id('payPassWord').send_keys('111111')
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(1)
        browser.switch_to_alert().accept()
        time.sleep(2)

    def get_ScreenShot(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = '..\\result\\image\\' + now + '.png'
        print pic_path
        browser.save_screenshot(pic_path)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid('logInCnaidai'))

    runner = unittest.TextTestRunner()
    runner.run(suite)