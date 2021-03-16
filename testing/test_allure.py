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


@allure.feature("登录模块")
class TestLogin():
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("step 1 - open"):
            print("step 1 - open login page")
        with allure.step("step 2 - input"):
            print("step 2 - type username and password")

        print("这是登录：测试用例 - 登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例 - 登录失败")
        assert 1 == 2
        pass

    @allure.story("登录失败 - 用户名缺失")
    def test_login_fail_no_username(self):
        print("这是登录：测试用例 - 登录失败 - 用户名缺失")
        pass

    @allure.story("登录失败 - 密码缺失")
    def test_login_fail_no_password(self):
        print("这是登录：测试用例 - 登录失败 - 密码缺失")
        pass


if __name__ == '__main__':
    pytest.main()