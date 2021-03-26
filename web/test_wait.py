from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://ceshiren.com/")

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_id("ember27").click()
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@title="the most active topics in the last year, month, week or day"]')) >= 1
        # WebDriverWait(self.driver, 10).until(wait)

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@title="the most active topics in the last year, month, week or day"]')))

        self.driver.find_element_by_xpath('//*[@title="topics with recent posts"]').click()