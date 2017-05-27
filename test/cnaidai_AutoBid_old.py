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

    def logInCNAiDai(self):
        browser.get(u'http://www.cnaidai.com/webpc/index.html')
        time.sleep(2)
        browser.find_element_by_xpath(u'/html/body/div[11]/div').click()
        time.sleep(2)
        browser.find_element_by_xpath(u'/html/body/div[2]/div/ul/li[4]/a').click()
        print (u'---->: 关闭广告宣传弹窗\n---->: 进入老版爱贷登录页……')
        # stepNum += 1
        time.sleep(1)

        # 开始输入用户名和密码以及验证码
        print(u'---->: 开始输入用户信息进行登录……')
        usernameLabel = browser.find_element_by_name(u'username')
        usernameLabel.clear()
        usernameLabel.send_keys(Keys.F11, u'wz001')
        print(u'---->: 输入用户名……')
        passwordLabel = browser.find_element_by_name(u'password')
        passwordLabel.clear()
        passwordLabel.send_keys(u'a1111111')
        print(u'---->: 输入密码……')
        valicodeLabel = browser.find_element_by_name(u'valicode')
        valicodeLabel.clear()
        valicodeLabel.send_keys(u'1111')
        print(u'---->: 输入验证码……')
        time.sleep(1)
        browser.find_element_by_id(u'login_submit').click()
        print(u'---->: 开始登录老平台……')
        time.sleep(5)
        browser.refresh()
        time.sleep(1)
        self.check_user_info_authentication_state()
        time.sleep(1)
        # global autoState
        # autoState = self.checkAutoState()
        # print(autoState)

    def check_user_state(self):
        print(u'---->: 开始验证用户状态……')

    def check_user_info_authentication_state(self):
        print(u'---->: 开始验证用户认证状态……')
        session = requests.session()
        loginURl = u'http://a.cnaidai.com/webjr/uc/indexCfg/account/userInfo.cgi?'
        uTime = int(time.mktime(datetime.datetime.now().timetuple()) * 1000)
        loginData = {u'_': uTime}
        userInfo = session.post(loginURl, data=loginData)
        print(userInfo)
        dic_json = json.dumps(userInfo.json(), sort_keys=True, indent=10, ensure_ascii=False)
        dicInfo = json.loads(dic_json)
        print (u'---->: Response : ', dicInfo)
        if dicInfo[u'message'] != u'请先登录':
            userInfo_detail = int(dicInfo[u'detailuser'])
            print(u'---->: 用户详细信息：', userInfo_detail)
            isPhoneAuth = userInfo_detail[u'phoneStatus']
            if isPhoneAuth == u'1':
                print(u'已验证手机号码')
            else:
                print(u'未验证手机号码')
            isRealName = userInfo_detail[u'realStatus']
            if isRealName == u'1':
                print(u'已实名认证')
            else:
                print(u'未实名认证')
            isOpenAutoBid = dicInfo[u'openAutoTender']
            if isOpenAutoBid == u'1':
                print(u'---->: 已开启自动投标')
            else:
                print(u'---->: 未开启自动投标')
        else:
            print(u'---->: 登录失败，请先登录')
        global auth_code
        #auth_code(phone,realName,bankCard)
        auth_code = u'000'


    def checkAutoState(autoState_check):
        print ('---->: 开始检查自动投标状态……')
        time.sleep(5)
        autoBtnText = browser.find_element_by_id('openAutoTender').text
        print autoBtnText
        if autoBtnText == '已开启 >':
            print('---->: 自动投标已开启')
            autoState_check = '1'
            # print('---->: Start to modify Automatic_Bid')
            # browser.find_element_by_id('openAutoTender').click()
        elif autoBtnText == '未开启 >':
            print('---->: 自动投标未开启')
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
            print('---->: 不能获取是否开启自动投标')
            autoState_check = '5'
        print(autoState_check)
        return autoState_check

    def open_Automatic_Bid(self):
        print('---->: 点击switch开关')
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
        browser.find_element_by_class_name(u'revise-btn').click()
        print(u'---->: 进入修改页面')
        time.sleep(2)
        print(u'---->: 选取年化率')
        # browser.find_element_by_id('minimumProfit').click()
        # time.sleep(1)
        selMin = browser.find_element_by_id(u'minimumProfit')
        selMax = browser.find_element_by_id(u'maximumProfit')
        numMin = random.randint(1,24)
        numMax = random.randint(1,24)
        while (numMin > numMax) :
            numMax = random.randint(1, 24)
        print (u'---->: 最小是: ', numMin, u'    最大是: ', numMax)
        time.sleep(1)
        Select(selMin).select_by_index(numMin - 1)
        time.sleep(1)
        Select(selMax).select_by_index(numMax - 1)
        time.sleep(1)
        for i in range(0, 5):
            dateIndex = random.randint(1, 5)
            print (u'dateIndex: ', dateIndex)
            if dateIndex == 1:
                browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(1)').click()
                time.sleep(1)
            elif dateIndex == 2:
                browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(2)').click()
                time.sleep(1)
            elif dateIndex == 3:
                browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(3)').click()
                time.sleep(1)
            elif dateIndex == 4:
                browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(4)').click()
                time.sleep(1)
            else:
                browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(3) > div.c > p > span:nth-child(5)').click()
                time.sleep(1)
        minAmount = random.randint(1, 10000) * 100
        maxAmount = random.randint(1, 10000) * 100
        while (minAmount > maxAmount):
            maxAmount = random.randint(1, 10000) * 100
        print(u'---->: 最小金额是: ', minAmount, u'    最大金额是: ', maxAmount)
        time.sleep(3)
        minAmount = browser.find_element_by_id(u'minimumAmount')
        minAmount.send_keys(Keys.LEFT_CONTROL, u'a')
        minAmount.send_keys(Keys.DELETE)
        minAmount.send_keys(minAmount)
        time.sleep(2)
        maxAmount = browser.find_element_by_id(u'maximumAmount')
        # minAmount.send_keys(Keys.LEFT_CONTROL, 'a')
        # minAmount.send_keys(Keys.DELETE)
        # maxAmount.send_keys(int(maxAmount * 100))
        time.sleep(2)

        discount_ticket = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(1)')
        interest_add_ticket = browser.find_element_by_css_selector(u'#main > div > div.user_right > div.m-set > div:nth-child(5) > div.c > div > label:nth-child(2)')

        ticketIndex = random.randint(1, 3)
        print(u'---->: 优惠券选取：', ticketIndex, u'<1：加息券；2：折扣券：3：全部选择>')
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

        print(u'---->: 点击设置并保存按钮')
        browser.find_element_by_class_name(u'btn-save').click()
        time.sleep(1)
        browser.find_element_by_id(u'payPassWord').send_keys(u'111111')
        time.sleep(1)
        browser.find_element_by_class_name(u'btn-ensure').click()
        time.sleep(1)
        browser.switch_to_alert().accept()

    def close_Automatic_Bid(self):
        print(u'---->: 开始关闭自动投标\n---->: 点击switch按钮')
        browser.find_element_by_id(u'openAutoTender').click()
        time.sleep(1)
        browser.find_element_by_class_name(u'open1').click()
        time.sleep(1)
        browser.find_element_by_id(u'payPassWord').send_keys(u'111111')
        time.sleep(1)
        browser.find_element_by_xpath(u'/html/body/div[6]/div[2]/a[2]').click()
        time.sleep(1)
        browser.switch_to_alert().accept()
        time.sleep(2)

    def get_ScreenShot(self):
        now = time.strftime(u'%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = u'..\\result\\image\\' + now + u'.png'
        print pic_path
        browser.save_screenshot(pic_path)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid(u'logInCNAiDai'))

    runner = unittest.TextTestRunner()
    runner.run(suite)