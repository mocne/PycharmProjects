#coding = utf-8
import unittest
import requests
from selenium import webdriver
import json
import re
import time

class modifiedPhoneNum(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10.0)
        self.driver.maximize_window()
        self.loginNum = "13000000000"
        self.loginPwd = "666666"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

        '''调用login函数'''
        self.login()
        # 列出一些测试需要的数据
        self.phoneNumList = [1234564567890, 12345645669, 10000000000,11012345678,16212346789, 19256456489,69894548755,53245678956,' ']
        self.verifyCodeList = [3232,55444,668,985999,'fdfd','yuh7',' ']
        self.pwd = [454578,12345,123456789012345678901,'yuhi','']
        global modifXpath                                                                                  #修改手机号按钮
        modifXpath = "me__number___gR8Vt"
        global phoneXpath
        phoneXpath= "/html/body/div[5]/div/div/div[1]/div/div[1]/input"
        global sendXpath
        sendXpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/button"
        global verifyCodeXpath
        verifyCodeXpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/input"
        global passWdXpath
        passWdXpath = "/html/body/div[5]/div/div/div[1]/div/div[3]/input"
        global cancelXpath
        cancelXpath ="dialog__dialog-button-cancel___tJdyZ"
        global confirmXpath
        confirmXpath = "/html/body/div[5]/div/div/div[2]/button[1]"
        global tipXpath
        tipXpath = "/html/body/div[5]/div/div/div[1]/div/span"
        self.tipText = ""
        self.verifyCode = ""
        self.inputVerifyCode = "5625"

    # 登录
    def login(self):
        self.driver.get("http://192.168.4.15:8001/1.8.0/cn/")
        loginPhoneNumBtn = self.driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/div/section/div/p[1]/input")
        loginPwdBtn = self.driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/div/section/div/p[2]/input")
        loginBtn =self.driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/div/section/p[1]")
        loginPhoneNumBtn.send_keys(self.loginNum)
        loginPwdBtn.send_keys(self.loginPwd)
        loginBtn.click()
        # 定位到用户头像的下拉列表
        profileBtn =self.driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/span")
        profileBtn.click()
        meInfoBtn = self.driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a")
        meInfoBtn.click()

    def reqVerifyCode(self):
        # 网络请求获取验证码
        verifyUrl = 'http://192.168.4.15:8001/1.8.0/cn/api/0.2/aux/sendverifycode'
        verifyParams = {'mobile': '18258183861', 'type': '3'}
        verify = requests.post(verifyUrl, data=verifyParams, headers=self.headers)
        print(verify.status_code)
        dic_json = json.dumps(verify.json(), sort_keys=True, indent=10, ensure_ascii=False)
        dicVerify = json.loads(dic_json)
        print(dicVerify)
        self.verifyCode = int(dicVerify["r"]["code"])

    # 断言与验证
    def confirmTest(self):
        try:
            tip = self.driver.find_element_by_xpath(tipXpath).text
            state = True
            if tip == self.tipText:
                self.assertTrue(True, ['正常'])
            else:
                self.assertFalse(False, tip)
        except:
            print("error")

    #修改手机号码----验证手机号码的合法性
    def test_PhoneNum_1(self):
        self.driver.find_element_by_class_name(modifXpath).click()
        #取消修改
        # self.driver.find_element_by_class_name(cancelXpath)
        #输入手机号：正则匹配复合手机号格式的手机号
        for phoneNum in self.phoneNumList:
            phoneNumInput = self.driver.find_element_by_xpath(phoneXpath)
            phoneNumInput.clear()
            phoneNumInput.send_keys(phoneNum)
            regex = "^1(3|4|5|7|8)\d{9}$"
            match = re.search(regex, "%s" %phoneNum)
            time.sleep(0.5)
            vertifyBtn = self.driver.find_element_by_xpath(sendXpath)
            vertifyBtn.click()
            if match:
                print("手机号合法是：%s" %phoneNum)
            else :
                self.tipText = "手机号码异常!"
                print("异常手机号是：%s" %phoneNum)
        print("test_PhoneNum_1---end")

    # 修改手机号码----验证码
    def test_verifyCode(self):
        #进入修改手机号的弹窗并发送验证码
        self.driver.find_element_by_class_name(modifXpath).click()
        self.driver.find_element_by_xpath(phoneXpath).send_keys(int(self.loginNum))
        # 获取验证码有效剩余时间
        time.sleep(3)
        vertifyBtn = self.driver.find_element_by_xpath(sendXpath)
        if  vertifyBtn.is_enabled():
            vertifyBtn.click()
            # 输入验证码和密码并确定来验证验证码的正确性
            self.driver.find_element_by_xpath(verifyCodeXpath).send_keys(self.inputVerifyCode)
            self.driver.find_element_by_xpath(passWdXpath).send_keys(self.loginPwd)
            # 取出文本中的数字
            restSeconds = self.driver.find_element_by_class_name("me__send-code___3uCe0").text
            restSeconds = int(re.sub("\D", "", restSeconds))
            print(restSeconds)
            time.sleep(2)
            if  restSeconds>0:
                self.driver.find_element_by_xpath(confirmXpath).click()
                if self.inputVerifyCode == self.verifyCode:
                    print("验证码输入正确")
                else:
                    print("验证码输入错误")
            else:
                self.driver.find_element_by_xpath(confirmXpath).click()
                print("验证码输入错误-----超时")
            print("test_verifyCode---end")
        else:
            print(2222)

    def test_password(self):
        testPwd = "123456"
        self.driver.find_element_by_xpath(passWdXpath).send_keys(testPwd)
        print("密码")

    def test_modifiedPhoneNum_2(self):
        print("testcase_2")

    #
    # def test_modifiedPhoneNum_3(self):
    #     print("testcase_3")

    # def tearDown(self):
        self.driver.quit()
        print("test end")

if __name__ == '__main__':
#
    suite = unittest.TestSuite()
    suite.addTest(modifiedPhoneNum("test_PhoneNum_1"))
    # suite.addTest(modifiedPhoneNum("test_verifyCode"))
#     # suite.addTest(modifiedPhoneNum("test_modifiedPhoneNum_3"))
#
    runner = unittest.TextTestRunner()
    runner.run(suite)


