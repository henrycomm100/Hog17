from time import sleep

from selenium.webdriver import ActionChains

from web.selenium_js.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element_by_xpath("//*[@id='draggable']")
        drop = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()
        sleep(2)

        self.driver.switch_to_alert().accept()

        sleep(2)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(2)
