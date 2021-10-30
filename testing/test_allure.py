import pytest
import allure


@allure.epic("用户管理")
@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_search_success(self):
        print("这是搜索：测试用例 - 搜索成功")
        pass

    @allure.story("搜索失败")
    def test_search_fail(self):
        print("这是搜索：测试用例 - 搜索失败")
        pass


@allure.feature("login")
class TestLogin():
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("login_success")
    @allure.title("登录成功")
    def test_login_success(self):
        with allure.step("step 1 - open"):
            print("step 1 - open login page")
            allure.attach("这是一个文本描述 allure attach text", attachment_type=allure.attachment_type.TEXT)
        with allure.step("step 2 - input"):
            print("step 2 - type username and password")
            allure.attach("<body>这是一个HTML</br> allure attach html</body>", "HTML测试块",
                          attachment_type=allure.attachment_type.HTML)

        print("这是登录：测试用例 - 登录成功")
        pass

    @allure.story("login_fail")
    @allure.description("登录失败的场景测试 - allure description")
    @allure.title("登录失败")
    @allure.testcase(
        "https://dev.azure.com/Comm100/Main/_queries/query/88115a63-17cb-466c-859a-4e186768f213/?fullScreen=false",
        'test case for login fail')
    def test_login_fail(self):
        print("这是登录：测试用例 - 登录失败")
        allure.attach.file("/Users/henry/PycharmProjects/Hog17/data/southparkavatar.png", name="这是一个图片",
                           attachment_type=allure.attachment_type.PNG)

        assert False
        pass

    @allure.story("login_fail_no_username")
    @allure.title("登录失败 - 没有用户名")
    def test_login_fail_no_username(self):
        print("这是登录：测试用例 - 登录失败 - 用户名缺失")
        allure.attach.file("/Users/henry/Movies/犬之岛HD美版中英双字.mp4", name="这是一个视频",
                           attachment_type=allure.attachment_type.MP4)

        pass

    @allure.story("login_fail_no_password")
    def test_login_fail_no_password(self):
        print("这是登录：测试用例 - 登录失败 - 密码缺失")
        pass


if __name__ == '__main__':
    pytest.main()