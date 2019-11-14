# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://555.0234.co/pc/index.html")
        driver.find_element_by_name("passwd").clear()
        driver.find_element_by_name("passwd").send_keys("123456")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='登 录'])[1]/preceding::div[9]").click()
        driver.find_element_by_id("account").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("dajunadmin")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='欢迎光临旺旺彩科技网站管理后台'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[1]/following::button[1]").click()
        driver.find_element_by_link_text(u"提现").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上 月'])[1]/following::button[1]").click()
        driver.find_element_by_id("render-canvas").click()
        driver.find_element_by_id("render-canvas").click()
        driver.find_element_by_id("render-canvas").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='竞技彩'])[1]/following::span[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
