from Base.base import Base
from Page.ele_page import ElePage
""" 定义搜索页面的类"""


class SearchPage(Base):
    def __init__(self):
        # 重写父类
        super().__init__()

    def click_search_btn(self):
        """点击搜索按钮结果"""
        self.click_ele(ElePage.search_btn)

    def input_search_text(self, text):
        """输入搜索内容"""
        self.send_ele(ElePage.search_input, text)

    def get_search_result(self):
        result = self.search_eles(ElePage.search_result)
        return [i.text for i in result]
