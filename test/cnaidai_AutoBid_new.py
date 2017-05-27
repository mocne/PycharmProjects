#coding: utf-8
__author__ = 'pkf'

from selenium import webdriver
import time,os,sys
import unittest,random
from selenium.webdriver.support.ui import Select

class Automatic_Bid(unittest.TestCase):

    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        global browser
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(10.0)

    def logInCnaidai(self):
        browser.get("http://a.cnaidai.com/webjr/login.htm")
        print ("---->: Come_to_Cnaidai_loginPage")
        # stepNum += 1
        time.sleep(1)

        print("---->: Start to input userMessage")
        usernameLabel = browser.find_element_by_name("username")
        usernameLabel.clear()
        usernameLabel.send_keys("13700120012")
        print("---->: input username")
        time.sleep(1)
        passwordLabel = browser.find_element_by_name("password")
        passwordLabel.clear()
        passwordLabel.send_keys("a1111111")
        print("---->: input password")
        time.sleep(1)
        valicodeLabel = browser.find_element_by_name("valicode")
        valicodeLabel.clear()
        valicodeLabel.send_keys("1111")
        print ("---->: input valicode")
        time.sleep(1)
        browser.find_element_by_id("login_submit").click()
        print ("---->: Log_into_Cnaidai")
        time.sleep(3)
        self.checkAutoState()
        browser.quit()

    def checkAutoState(self):
        print ("---->: Start_checkAutoBidState")
        autoBtnText = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/a").text
        if autoBtnText == "查看":
            print("---->: Automatic_Bid is Open")
            self.modify_Automatic_Bid()
            time.sleep(5)

            self.close_Automatic_Bid()
            time.sleep(5)

        else:
            print("---->: Automatic_Bid is Close")
            self.open_Automatic_Bid()
            time.sleep(5)

        time.sleep(5)

    def open_Automatic_Bid(self):
        print("---->: start to open Automatic_Bid")
        time.sleep(3)
        # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/a").click()
        browser.find_element_by_css_selector("body > div.g-bd > div > div.user_right > div.J-autoTender > a").click()
        # browser.find_element_by_link_text("立即参与").click()
        # 100<=x<=1000000
        minNum = random.randint(1,10000)
        browser.find_element_by_name("minMum").send_keys(minNum * 100)
        maxNum = random.randint(0,10001)
        while maxNum <= minNum:
            maxNum = random.randint(1,10000)
        browser.find_element_by_name("maxMum").send_keys(maxNum * 100)
        # browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/cite/p/em").click()
        # browser.find_element_by_xpath("").click()
        select = Select(browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/cite/p/em"))
        select.select_by_index(random.randint(0,23))

        browser.find_element_by_name("openBtn").click()

    def modify_Automatic_Bid(self):
        print("---->: start to modify Automatic_Bid")

    def close_Automatic_Bid(self):
        print("---->: start to close Automatic_Bid")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid("logInCnaidai"))

    runner = unittest.TextTestRunner()
    runner.run(suite)