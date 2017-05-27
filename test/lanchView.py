from selenium import webdriver
import time,os,sys

stepNum = 1
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://www.cnaidai.com/")
print stepNum,": Come in First_Page"
stepNum += 1
time.sleep(3)


browser.find_element_by_xpath("/html/body/div[12]/div").click()
print stepNum,': Quit_AlarmView'
stepNum += 1
time.sleep(3)

browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img").click()
print stepNum,": Click_logoIMG"
stepNum += 1
time.sleep(3)

browser.find_element_by_id("username").click()
print stepNum,": Click_Register"
stepNum += 1
time.sleep(2)

browser.find_element_by_css_selector("#userName").send_keys("18267175336")
print stepNum,": Input_PhoneNumber"
stepNum += 1
time.sleep(2)
browser.find_element_by_id("valicode").send_keys("1234")
print stepNum,": Input_Auth_Code"
stepNum += 1
time.sleep(2)
browser.find_element_by_class_name("valcode").click()
print stepNum,": Send_PhoneMessage"
stepNum += 1
time.sleep(10)
browser.find_element_by_css_selector("#phoneCode").send_keys("123456")
print stepNum,": Input_Phone_Auth_Code"
stepNum += 1
time.sleep(2)


