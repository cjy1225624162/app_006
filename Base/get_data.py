import os

import yaml


"""
获取当前文件的绝对路径     current_path = os.path.abspath(__file__)
获取当前文件所在目录       os.path.dirname(os.path.abspath(__file__))
          os.path.realpath(__file__)
"""

class GetData:
    """读取测试数据"""
    @classmethod
    def get_yaml_data(cls, name):
        """读取yaml数据"""

        # 打开文件
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # yaml读取文件
            return yaml.safe_load(f)

