# -*- coding: utf-8 -*-

import time
import Register_aidaiwangApp

def start_to_logout():

    driver = Register_aidaiwangApp.driver

    print(u'logout')
    time.sleep(3)
    try:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine')
        print('id')
    except:
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
        except:
            return 'can not jump to mine'
        else:
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
            print('text')
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine').click()

    try:
        driver.find_element_by_id('cn.phaidai.loan:id/iv_right')
    except:
        return 'can not jump into setting page'
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/iv_right').click()
        try:
            driver.find_element_by_id('cn.phaidai.loan:id/tv_exit')
        except:
            return 'can not found logout key'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/tv_exit').click()
            driver.find_element_by_id('cn.phaidai.loan:id/iv_left').click()
            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            except:
                try:
                    driver.find_element_by_id('cn.phaidai.loan:id/rb_home').click()
                except:
                    return 'can not jump to shouye after logout'