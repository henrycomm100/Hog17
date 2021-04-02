from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestTouchActions:
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("https://www.bing.com/")

        ele_keyword = self.driver.find_element_by_id("sb_form_q")
        ele_search = self.driver.find_element_by_xpath("//*[@id='sb_form']/label")

        ele_keyword.send_keys("henry")

        action = TouchActions(self.driver)
        action.tap(ele_search)

        action.perform()
        sleep(3)

        ele_search2 = self.driver.find_element_by_id("sb_form_go")
        ele_search2.click()
        action.scroll_from_element(ele_search2, 0, 10000).perform()
        sleep(3)

    def test_baidu_click(self):
        self.driver.get("https://www.baidu.com/")

        ele_keyword = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele_keyword.send_keys("henry")

        action = TouchActions(self.driver)
        action.tap(ele_search)

        action.perform()

        action.scroll_from_element(ele_keyword, 0, 10000).perform()
        sleep(3)
