# -*- coding: utf-8 -*-
__author__ = 'pkf'
from selenium import webdriver
import time

stepNum = 1
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)
time.sleep(3)
browser.maximize_window()

browser.get("http://www.baidu.com/")
print stepNum,": Come in First_Page"
stepNum += 1
time.sleep(3)

browser.add_cookie({'name':'BAIDUID', 'value':'56AE9C6D8759585791B8159862766009:FG=1'})
browser.add_cookie({'name':'BIDUPSID', 'value':'F5D91E5E415BFC872D135B80FAD6B312'})
browser.add_cookie({'name':'BDORZ', 'value':'B490B5EBF6F3CD402E515D22BCDA1598'})
browser.add_cookie({'name':'BDUSS', 'value':'HZEdWtORkk5UXFyeH4zbC0zQmdXeExhLVIyVXk3bzJSek5IZlEtfjZZWG1wRXRaSVFBQUFBJCQAAAAAAAAAAAEAAAApaOAJw~zUy9TaztXK1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOYXJFnmFyRZZ'})
browser.add_cookie({'name':'BD_HOME', 'value':'1'})
browser.add_cookie({'name':'BD_UPN', 'value':'12314753'})
browser.add_cookie({'name':'FP_UID', 'value':'86e083ae9c21a972b7345e867b639cda'})
browser.add_cookie({'name':'H_PS_PSSID', 'value':'1429_19037_21115_18559_17001F'})
browser.add_cookie({'name':'ORIGIN', 'value':'0'})
browser.add_cookie({'name':'PSTM','value':'1495502251'})
browser.add_cookie({'name':'bdime','value':'0'})
browser.add_cookie({'name':'pgv_pvi','value':'8579155968'})
browser.add_cookie({'name':'sug','value':'3'})
browser.add_cookie({'name':'sugstore','value':'0'})
time.sleep(3)

print stepNum,": start to login"
browser.get("http://www.baidu.com/")
stepNum += 1
time.sleep(2)

logIn_mes = browser.find_element_by_css_selector("#s_username_top > span").text
try:
    assert logIn_mes == u'命运在握手'
    print ("    LogIn Success !")
except Exception as e:
    print ("    LogIn Fail.", format(e))
stepNum += 1
time.sleep(2)

# browser.find_element_by_link_text("贴吧").click()
# time.sleep(2)
#
# browser.back()
# time.sleep(2)
#
# browser.forward()
# time.sleep(2)

browser.quit()
print stepNum,": Browser Is Quit"
