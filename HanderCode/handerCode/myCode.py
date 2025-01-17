# -*- coding: utf-8 -*-

import time
import unittest

from DriverInit import initAppiumDriver


class AiDaiWangApp(unittest.TestCase):
    global driver
    driver = initAppiumDriver.initWithInfo('cn.phaidai.loan', 'com.rd.zdbao.adwjk.activity.SplashActivity')

    def setUp(self):

        isInstall = driver.is_app_installed('cn.phaidai.loan')
        if isInstall:
            print('aidai.apk installed already')
        else:
            driver.install_app('./app/aidai.apk')
            if driver.is_app_installed('cn.phaidai.loan'):
                print('aidai.apk install success')
            else:
                print('install app failed')
            print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

    @staticmethod
    def test_loginAiDaiWangApp():
        print('test')

    @staticmethod
    def test_logoutAiDaiWangApp():
        pass


    def tearDown(self):
        print('test task ended')
        time.sleep(10)
        driver.close_app()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AiDaiWangApp('test_loginAiDaiWangApp'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
