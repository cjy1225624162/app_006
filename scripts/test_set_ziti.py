from Base.driver import Driver
from Base.page import Page
from Page.setting_page import SettingPage
from Page.xianshi_page import XianshiPage


class Test_Set_Ziti:

    def teartowm(self):
        # 关闭驱动
        Driver.quit_app_driver()

    def test_set_ziti(self):
        # 点击显示按钮
        Page.get_setting_page().click_xianshi()
        # 点击字体大小 # 选择字体为普通
        Page.get_xianshi_page().click_ziti_size()
        # 断言
        assert "普通" in Page.get_xianshi_page().get_ziti_results()
