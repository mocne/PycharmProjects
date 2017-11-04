# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.Chrome()

def findByID(driver, ID):
    try:
        driver.find_element_by_id(ID)
    except:
        return False
    else:
        el = driver.find_element_by_id(ID)
        return el

def findByCN(driver, CN):
    try:
        driver.find_element_by_class_name(CN)
    except:
        return False
    else:
        el = driver.find_element_by_class_name(CN)
        return el

def findByLT(driver, LT):
    try:
        driver.find_element_by_link_text(LT)
    except:
        return False
    else:
        el = driver.find_element_by_link_text(LT)
        return el

def findByXP(driver, XP):
    el = driver.find_element_by_xpath(XP)
    return el

def findByCS(driver, CS):
    el = driver.find_element_by_css_selector(CS)
    return el

def findByAI(driver, AI):
    el = driver.find_element_by_accessibility_id(AI)
    return el

def findAUByID(driver, ID):
    el = driver.find_element_by_android_uiautomator('new UiSelector().id(%s)' % ID)
    return el

def findAUByTEXT(driver, TEXT):
    el = driver.find_element_by_android_uiautomator('new UiSelector().text(%s)' % TEXT)
    return el

def findAUByDescription(driver, description):
    el = driver.find_element_by_android_uiautomator('new UiSelector().description("%s")' % description)
    return el

def findsByCN(driver, CN, index):
    el = driver.find_elements_by_class_name(CN)[index]
    return el

def inputText(el, text):
    el.click()
    el.clear()
    el.send_keys(text)

def doWithParm(driver, beheaver, parm, behaver1, parm1):
    if beheaver == 'get':
        try:
            driver.get(parm)
        except:
            return False
        else:
            return True
    elif beheaver == 'clickXpath':
        try:
            driver.find_element_by_xpath(parm)
        except:
            return False
        else:
            driver.find_element_by_xpath(parm).click()
    elif beheaver == 'checkClass':
        try:
            driver.find_element_by_class_name(parm)
        except:
            return False
        else:
            return True
    elif beheaver == 'checkImgSizeByXpath':
        try:
            driver.find_element_by_xpath(parm)
        except:
            return False
        else:
            for image in driver.find_element_by_xpath(parm):
                if image.size != (92, 40):
                    return False
            return True