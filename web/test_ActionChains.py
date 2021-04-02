from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")

        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)

        sleep(3)
        action.perform()
        sleep(3)

    def test_move(self):
        self.driver.get("https://www.baidu.com/")
        element_settings = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)

        action.move_to_element(element_settings)
        action.perform()
        sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element_by_id("dragger")
        # element_drop = self.driver.find_element_by_xpath("/html/body/div[5]")
        element_drop = self.driver.find_element_by_css_selector("div:nth-last-child(1)")

        action = ActionChains(self.driver)

        # action.drag_and_drop(element_drag, element_drop)
        action.click_and_hold(element_drag).release(element_drop)
        action.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        input1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")

        action = ActionChains(self.driver)

        action.click(input1)
        action.send_keys('username')
        sleep(2)
        action.send_keys(Keys.SPACE)
        sleep(2)
        action.send_keys('tom')
        sleep(2)
        action.send_keys(Keys.BACKSPACE)
        sleep(2)
        action.perform()
        sleep(2)
