import threading

import selenium
from selenium import webdriver
import pytest
import time
import json

from selenium.webdriver.chrome.options import Options


# driver = webdriver.Chrome();

# 创建Chrome浏览器的一个Options实例对象
chrome_options = Options()
# 添加屏蔽--ignore--certificate--errors提示信息的设置参数项
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])


class TestDemotest():
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",
                              chrome_options=chrome_options)

    def setup_method(self):
        self.vars = {}
        self.driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")
        # self.driver.add_cookie({'name': 'cpanelauth',
        #                         'value': '%2bZ4qviC7edNnEEDvAdy4J9lXEPPfsQawA9lbqgPYTyBkJx6dCn6h%2ftRPkT0HqmjrAf4pMs2Sgfx8Y8X7OY2nWQRhunD9OnaXyUiqlVdPtpw%3d'})

        self.driver.find_element_by_id("email").send_keys("Carl.zhou@comm100.com")
        self.driver.find_element_by_id("pwd").send_keys("111111")
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div[4]/input").click()
        time.sleep(5)
        self.driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")

    def teardown_method(self, method):
        pass
        # self.driver.quit()

    def test_screenshot(self):
        # driver = self.driver
        chat_server_urls = [
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5000808',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5001112',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=5001843',
            'https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=60000988'
        ]
        # 每隔300秒截屏一次
        # t = threading.Timer(300, self.test_screenshot)
        # t.start()

        while (True):
            while (True):
                print(" begin sleep 290s")
                time.sleep(290)
                self.driver.refresh()
                print("sleep and  refresh finished")
                break

            for i in range(0, 5):
                print("begin to take screenshot from site to site")
                self.driver.get(chat_server_urls[i])
                time.sleep(5)
                if i == 0:
                    print("screenshot site1")
                    # self.driver.get_screenshot_as_file(rf"C:\Users\comm100\PycharmProjects\Hog17\demo\node{i + 1}\%s.png" % time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
                    self.driver.get_screenshot_as_file(
                        rf"d:\\10000\\%s.png" % str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))))
                    time.sleep(3)

                elif i == 1:
                    print("screenshot site2")
                    self.driver.get_screenshot_as_file(
                        rf"d:\\5000808\\%s.png" % (
                            str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))))
                    time.sleep(3)

                elif i == 2:
                    print("screenshot site3")
                    self.driver.get_screenshot_as_file(
                        rf"d:\\5001112\\%s.png" % str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))))
                    time.sleep(3)

                elif i == 3:
                    print("screenshot site4")
                    self.driver.get_screenshot_as_file(
                        rf"d:\\5001843\\%s.png" % str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))))
                    time.sleep(3)

                elif i == 4:
                    print("screenshot site5")
                    self.driver.get_screenshot_as_file(
                        rf"d:\\60000988\\%s.png" % time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
                    time.sleep(3)



if __name__ == '__main__':
    testd = TestDemotest()
    testd.setup_method()
    testd.test_screenshot()
