import json
from time import sleep

from selenium import webdriver


class TestCookieLogin:
    def setup(self):
        # # 需要复用Chrome时使用debug选项
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)

        # #不需要复用时，直接使用如下
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login_use_cookie(self):
        # # !!先运行这一步。
        # # 需要先从已经登录的浏览器中将cookie拿出来，可以使用chrome debug去复用浏览器的方式将cookie取过来
        # cookies = self.driver.get_cookies()
        # # print(cookies)
        # with open('cookie.txt', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(cookies)) # 或者可以直接这么写：json.dump(cookies)

        # 读取文件中的cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        with open('cookie.txt', 'r', encoding='utf-8') as f:
            raw_cookies = f.read()
            cookies = json.loads(raw_cookies)
            # 或者上面两句可以直接使用 cookies = json.load(f)

        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
