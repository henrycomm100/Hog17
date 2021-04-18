from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in?locale=en')
        self.driver.find_element_by_id('user_login').send_keys('henryhappier')
        self.driver.find_element_by_id('user_password').send_keys('Aa999999')

        # 直接找到checkbox的input，然后去执行click()会报错，"error":"element click intercepted"
        # 后来只能换成了，去点击整个remember me的div，或者是remember me的label元素，这样就可以执行成功了
        # self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div').click()
        ele_remember_label = self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div/label')
        ele_remember_label.click()
        sleep(3)

        # 经过跟Bruce讨论之后，有如下两个新的解决方案：
        # 1. 使用execute_script的方法来执行click动作
        ele_remember_input = self.driver.find_element_by_xpath('//*[@id="user_remember_me"]')
        self.driver.execute_script('arguments[0].click();', ele_remember_input)
        sleep(3)

        # 2. 使用ActionChains的move_to_element然后再执行click动作
        ActionChains(self.driver).move_to_element(ele_remember_input).click()
        sleep(3)

        self.driver.find_element_by_name('commit').click()
        sleep(3)

    def test_comm100_login_form(self):
        self.driver.get('https://secure.comm100.com/login.aspx')
        self.driver.find_element_by_id('chkAutoLogin').click()
        sleep(3)
