from selenium import webdriver
import threading
import time
import os

def auto_screenshot():

    # 初始化一个谷歌浏览器实例
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")
    driver.add_cookie({'name': 'cpanelauth',
                       'value': '%2bZ4qviC7edP%2fZg7qkQefzAFnqQK0Gm%2bo%2b8R%2br2B0KLISdcbAnl8hmUtN4PCXLhrMcg9V4zB4A6shD8duYPWJ%2fEdNF4CokrNqtIfwREUoOJY%3d'})

    driver.get("https://chatserver1.livelyhelp.chat/statistic.aspx?siteid=10000")


    # 每隔90秒截屏一次
    t = threading.Timer(1200, auto_screenshot)
    t.start()

    driver.refresh()

    driver.get_screenshot_as_file(r"C:\Users\comm100\PycharmProjects\Hog17\demo\%s.png" %time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))

    print(os.getcwd())
    # driver.quit()


if __name__ == "__main__":
    auto_screenshot()

