from time import sleep
import random

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestContacts:
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_contacts(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()

        # 一定要重新定义一遍driver, 然后重新用新的driver去获取一遍add_member按钮（print语句）。
        # 不然又会遇到stale element reference的错误.
        driver = self.driver
        driver.refresh()
        print(len(driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")))
        # element_add_member = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1]
        # element_add_member.click()
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
        account_id = "userEric" + str(random.randint(1, 1000000))
        email = account_id + "@hh.com"
        self.driver.find_element_by_id("username").send_keys(account_id)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(account_id)
        self.driver.find_element_by_id("memberAdd_mail").send_keys(email)
        self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()

        sleep(3)
