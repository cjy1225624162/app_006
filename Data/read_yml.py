import os

import pytest
import yaml

from Base.get_data import GetData


def sum_data():
    # 定义空列表存数数据
    sum_list = []
    # 通过GetData函数打开文件
    data = GetData.get_yaml_data("sum.yml")
    # print("data:", data)
    # print("values:", data.values())
    for i in data.values():
        # print("i", i)
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list


def search_data():
    # 定义空列表存储数据
    search_list = []
    # 读取data
    data = GetData.get_yaml_data("search.yml")
    for i in data.values():
        search_list.append((i.get("search_data"), i.get("search_result")))
    return search_list
