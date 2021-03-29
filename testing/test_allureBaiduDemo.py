import pytest
from selenium import webdriver


def test_baidudemo():
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("https://www.baidu.com")
    driver.quit()

