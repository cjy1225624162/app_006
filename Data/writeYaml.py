import yaml

data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}


# 打开文件
with open("./abc.yml", "a", encoding="utf-8") as f:
    # yaml写入数据
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode = True)
