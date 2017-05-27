from selenium import webdriver
import time,os,sys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)

browser.get("http://www.cnaidai.com/")
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[12]/div").click()
time.sleep(3)
browser.add_cookie({'name':'username', 'value':'hewen'})
browser.add_cookie({'name':'password', 'value':'a1111111'})
time.sleep(3)
browser.get("http://www.cnaidai.com/")
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[12]/div").click()
browser.quit()



