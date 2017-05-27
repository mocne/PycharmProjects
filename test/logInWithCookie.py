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

browser.add_cookie({'name':'BAIDUID', 'value':'56AE9C6D8759585791B8159862766009:FG=1'})
browser.add_cookie({'name':'BIDUPSID', 'value':'F5D91E5E415BFC872D135B80FAD6B312'})
browser.add_cookie({'name':'HMACCOUNT', 'value':'9B47006C00747802'})
time.sleep(3)

try:
    browser.refresh()
    print ('test pass: refresh successful')
except Exception as e:
    print ("Exception found", format(e))

browser.get("http://www.cnaidai.com/")
print stepNum,": Come in First_Page Again"
stepNum += 1
try:
    browser.refresh()
    print ('test pass: refresh successful')
except Exception as e:
    print ("Exception found", format(e))
time.sleep(30)

browser.quit()
print stepNum,": QUIT_Browser"
