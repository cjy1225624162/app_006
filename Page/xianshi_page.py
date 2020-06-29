from Base.base import Base
from Page.ele_page import ElePage


class XianshiPage(Base):
    """显示页面"""
    def __init__(self):
        super().__init__()

    def click_ziti_size(self):
        """点击字体大小和选择字体大小"""
        # 点击字体大小
        self.click_ele(ElePage.ziti_size)
        # 点击选择”普通“字体
        self.click_ele(ElePage.ziti_choose_pt)

    def get_ziti_results(self):
        result = self.search_eles(ElePage.ziti_style)
        return [i.text for i in result]
