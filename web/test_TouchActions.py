from time import sleep

import pytest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestTouchActions:
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_bing_click(self):
        self.driver.get("https://cn.bing.com/")

        ele_keyword = self.driver.find_element_by_id("sb_form_q")
        ele_search = self.driver.find_element_by_id("sb_form_go")

        ele_keyword.send_keys("henry")

        action = TouchActions(self.driver)
        action.tap(ele_search)

        action.perform()

        # 一定要重新去定义一遍action，然后重新去获取一次元素，不然会一直报stale element reference的错误。可以分别命名成new_action, new_ele_keyword以示区分
        action = TouchActions(self.driver)
        ele_keyword = self.driver.find_element_by_id('sb_form_q')

        action.scroll_from_element(ele_keyword, 0, 10000).perform()
        sleep(3)

    def test_bing_click2(self):
        self.driver.get(
            "https://cn.bing.com/search?q=henry&qs=n&form=QBLH&sp=-1&pq=henry&sc=6-5&sk=&cvid=A14643AF45204031BC59B0C3BE7DA600")

        ele_keyword = self.driver.find_element_by_id("sb_form_q")

        action = TouchActions(self.driver)
        action.scroll_from_element(ele_keyword, 0, 10000).perform()
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
