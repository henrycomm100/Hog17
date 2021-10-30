import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.feature("百度搜索")
class TestAllureBaiduDemo:
    @allure.feature("关键词搜索")
    @pytest.mark.parametrize("test_data", ["pytest", "allure", "bdd"])
    def test_allurebaidudemo(self, test_data):
        with allure.step("打开百度网页"):
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            # chrome_options.headless = True # also works
            driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
            driver.get("https://www.baidu.com")
            driver.maximize_window()
            driver.implicitly_wait(5)

        with allure.step(f"执行搜索：{test_data}"):
            driver.find_element_by_id("kw").send_keys(test_data)
            driver.find_element_by_id("su").click()
            time.sleep(2)

        with allure.step("保存截图"):
            driver.save_screenshot("./result/a.png")
            allure.attach.file("./result/a.png", "screenshot name", allure.attachment_type.PNG)

        with allure.step("关闭浏览器"):
            driver.quit()
