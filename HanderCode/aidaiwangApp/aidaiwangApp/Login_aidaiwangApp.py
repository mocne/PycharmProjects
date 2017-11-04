# -*- coding: utf-8 -*-

import time
import xlrd
import Register_aidaiwangApp
import LogOut_aidiawangApp

def start_to_login(filename):

    print(u'login')
    driver = Register_aidaiwangApp.driver
    driver.launch_app()
    time.sleep(3)
    try:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine')
        print('id')
    except:
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text(u"我的")')
        except:
            return 'can not jump to mine'
        else:
            driver.find_element_by_android_uiautomator('new UiSelector().text(u"我的")').click()
            print('text')
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine').click()

    try:
        driver.find_element_by_id('cn.phaidai.loan:id/tv_click')
    except:
        try:
            driver.find_element_by_id('cn.phaidai.loan:id/iv_avatar')
        except:
            return 'can not check status'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/iv_avatar').click()

    else:
        usernameLabel = driver.find_element_by_id('cn.phaidai.loan:id/tv_click')
        loginfo = usernameLabel.text
        while loginfo != u'立即登录':
            LogOut_aidiawangApp.start_to_logout()
        usernameLabel.click()

        currentAC = driver.current_activity
        print(currentAC)

        print(filename)
        userData = xlrd.open_workbook(r'%s' % filename)
        print('open user file success')

        userSheet = userData.sheet_by_name('login')
        loginName = str(userSheet.cell_value(1, 0))
        loginPassword = str(userSheet.cell_value(1, 1))

        print(loginName.split('.')[0], loginPassword)

        try:
            userNameLabel = driver.find_element_by_id('cn.phaidai.loan:id/et_login_name')
            userNameLabel.clear()
            userNameLabel.send_keys(loginName.split('.')[0])
        except:
            return 'can not input username : %s' % loginName.split('.')[0]
        driver.find_element_by_id('cn.phaidai.loan:id/et_login_password').send_keys(loginPassword)
        driver.find_element_by_id('cn.phaidai.loan:id/bt_login_into').click()
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text(u"首页")').click()
        except:
            driver.find_element_by_id('cn.phaidai.loan:id/rb_home').click()
