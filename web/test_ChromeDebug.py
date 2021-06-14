from time import sleep

from selenium import webdriver


class TestChromeDebug:
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_wework_login_using_chrome_debug(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        sleep(3)

    def test_goto_contacts(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
