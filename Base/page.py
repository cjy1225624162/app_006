from Page.search_page import SearchPage
from Page.setting_page import SettingPage
from Page.xianshi_page import XianshiPage


class Page:
    """定义实例化对象的类"""

    @classmethod
    def get_search_page(cls):
        """定义实例化搜索页面Page的方法"""
        return SearchPage()

    @classmethod
    def get_setting_page(cls):
        """定义设置页面Page的方法"""
        return SettingPage()

    @classmethod
    def get_xianshi_page(cls):
        """定义显示页面Page的方法"""
        return XianshiPage()
