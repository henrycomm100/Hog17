from time import sleep

from selenium.webdriver.common.keys import Keys
from web.selenium_js.base import Base
import pytest


class TestJS(Base):
    # @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # self.driver.find_element_by_id("kw").send_keys(Keys.RETURN)

        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()

        # 这里，一定要重新定义一遍driver，然后刷新一下页面，不然后面执行的document.documentElement.scrollTop=10000会一直无法生效。
        # 这个问题跟test_ActionChains.py中test_bing_click遇到的问题一样。
        driver = self.driver
        driver.refresh()
        print(driver.current_url)
        driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        print(driver.execute_script("return document.documentElement.scrollTop"))
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(2)
        print(self.driver.execute_script("return document.title, JSON.stringify(performance.timing)"))
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))  #
        # 不能写成这样，这样子的话只有前面的一个return才会起作用。

    def test_datetime_component(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value = '2021-05-30'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
