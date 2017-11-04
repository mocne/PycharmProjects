# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class aidaiwanglicai(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://cnaidai.com/")
        self.selenium.start()
    
    def test_aidaiwanglicai(self):
        sel = self.selenium
        sel.open("/")
        sel.click(u"link=我的账户")
        sel.wait_for_page_to_load("30000")
        sel.type("name=username", "18244440002")
        sel.type("name=password", "a1111111")
        sel.type("name=valicode", "1111")
        sel.click("id=J-loginBtn")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
