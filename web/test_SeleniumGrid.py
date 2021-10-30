import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSeleniumGrid:
    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub')
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("Henry")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.LINK_TEXT, "Henry(足球明星) - 百度百科")
        print(self.driver.current_url)
