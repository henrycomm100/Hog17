from selenium import webdriver
import threading
import time
import os


class TestAutoScreenshot:

    def setup(self):
        # 初始化一个谷歌浏览器实例
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")
        self.driver.add_cookie({'name': 'cpanelauth',
                                'value': '%2bZ4qviC7edP%2fZg7qkQefzAFnqQK0Gm%2bo%2b8R%2br2B0KLISdcbAnl8hmUtN4PCXLhrMcg9V4zB4A6shD8duYPWJ%2fIPLmH8Wbu9jsCQAoldb7IM%3d'})

        self.driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")

    def teardown(self):
        # driver.quit()
        pass

    def test_screenshot(self):
        driver = self.driver
        chat_server_urls = [
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5000808',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5001112',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5001843',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=60000988'
        ]
        # 每隔300秒截屏一次
        t = threading.Timer(360, self.test_screenshot)
        t.start()

        for i in range(0, 5):
            driver.get(chat_server_urls[i])
            driver.get_screenshot_as_file(
                rf"C:\Users\comm100\PycharmProjects\Hog17\demo\node{i + 1}\%s.png" % time.strftime('%Y-%m-%d-%H-%M-%S',
                                                                                                   time.localtime(
                                                                                                       time.time())))
