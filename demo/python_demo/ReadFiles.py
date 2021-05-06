# read files
import struct

f = open('../../data/footballClubs.txt')
print(f.readable())
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()

# with语句块，文件打开，操作完毕后，可以自动关闭文件
with open('../../data/footballClubs.txt') as f2:
    print(f2.readlines())

# 读取图片需要使用参数 rb
with open(('../data/southparkavatar.png'), 'rb') as f3:
    # context = f3.read(5)
    # realcontext = struct.unpack('4c',context)
    print(f3)