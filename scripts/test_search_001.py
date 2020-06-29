from appium import webdriver
import pytest, time
from selenium.webdriver.common.by import By
from Base.base import Base
from Base.driver import Driver
from Base.page import Page
from Page.search_page import SearchPage

from Data.read_yml import search_data

class Test_Search:

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮 并且 点击一次"""
        Page.get_search_page().click_search_btn()

    @pytest.mark.parametrize("search_data, exp_data", search_data())
    def test_search_text(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 输入框输入内容
        Page.get_search_page().input_search_text(search_data)
        # 获取结果
        # 断言
        assert exp_data in Page.get_search_page().get_search_result()
