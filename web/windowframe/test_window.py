from web.windowframe.base import Base
from time import sleep


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        window = self.driver.window_handles[-1]
        self.driver.switch_to_window(window)

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("henryhappier")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13500000000")

        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("henryhappier")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("Aa000000")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        sleep(3)
