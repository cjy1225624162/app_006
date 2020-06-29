from Base.base import Base
from Page.ele_page import ElePage


class SettingPage(Base):
    """设置页面"""
    def __init__(self):
        # 初始化父类方法
        super().__init__()

    def click_xianshi(self):
        """点击显示按钮"""
        self.click_ele(ElePage.xianshi)
