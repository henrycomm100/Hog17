# json由字典和列表组成
import json
import pprint

data = {
    "name": ["henry", "mj", "draper"],
    "age": 33,
    "gender": "male"
}

print(type(data))

# 将 Python 对象编码成 JSON 字符串
data1  = json.dumps(data)
print(data1)
print(type(data1))

pprint.pprint(data)

# 将已编码的 JSON 字符串解码为 Python 对象
data2 = json.loads(data1)
print(type(data2))
print(data2)