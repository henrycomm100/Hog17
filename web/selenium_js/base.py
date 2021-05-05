import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def setup(self):
        browser = os.getenv("browser")

        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":  # 这里我们不再使用PhantomJS，因为已经停止更新了。我们使用headless chrome
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            # chrome_options.headless = True # also works
            self.driver = webdriver.Chrome(options=chrome_options)
        elif browser == "safari":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
