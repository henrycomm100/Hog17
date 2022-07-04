# read files
import json
import struct

# f = open('../../data/footballClubs.txt')
# print(f.readable())
# print(f.readlines())  # 将所有行读出来
# # print(f.readline()) # 按行读取
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# f.close()

# # with语句块，文件打开，操作完毕后，可以自动关闭文件
# with open('../../data/footballClubs.txt') as f2:
#     print(f2.readlines())
#
# # 读取图片需要使用参数 rb
# with open(('../../data/southparkavatar.png'), 'rb') as f3:
#     context = f3.read(50)
#     # real_context = struct.unpack('4c', context)
#     print(f3)
#     print(context)
# #
# f = open('data.txt', 'w')
# print(f.readable())
# print(f.encoding)
# print(f.mode)
# print(f.name)
# print(f.writable())
# f.write('a \n b \n c \n hello')
#
# f.close()
#
# f = open('data.txt', 'r')
# print(f.readlines())
#
# f.close()

# # # 同时读写文件
# with open('data.txt', 'w+') as f:
#     print(f.mode)
#     print(f.name)
#     print(f.readable())
#     print(f.writable())
#
#     print(f.readlines())  # 此时，返回的是[]
#
#     f.write('1 \n 2 \n 3 \n changed')
#     print(f.readlines())  # 此时，返回的是[]
#
# # 重新打开文件 才可以读取到新的内容
# with open('data.txt', 'r') as f:
#     print(f.readlines())


# # # json
data = {
    "name": ["henry", "MJ"],
    "age": 30,
    "gender": "male"
}

print(type(data))  # 本身是dict类型
data1 = json.dumps(data)  # 将其转换为str
print(data1)
print(type(data1))

data2 = json.loads(data1)  # 将str重新转换为json
print(type(data2))
