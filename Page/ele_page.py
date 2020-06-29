from selenium.webdriver.common.by import By
"""定义页面元素类"""


class ElePage:
    """管理页面所有元素"""
    """---搜索按钮页面---"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 搜索输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    """---设置页面---"""
    # 显示
    xianshi = (By.XPATH, "//*[contains(@text,'显示')]")

    """---显示页面---"""
    # 字体大小
    ziti_size = (By.XPATH, "//*[contains(@text, '字体大小')]")
    # 选择字体大小--普通
    ziti_choose_pt = (By.XPATH, "//*[contains(@text, '普通')]")
    # 字体大小描述信息
    ziti_style = (By.ID, "android:id/summary")
