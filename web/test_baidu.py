from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, "kw").send_keys("Henry")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.LINK_TEXT, "Henry(足球明星) - 百度百科")