from time import sleep

from web.selenium_js.base import Base


class TestFileUpload(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("stfile").send_keys(
            "/Users/henry/PycharmProjects/Hog17/web/fileupload_alert/image/stats.png")
        sleep(5)
