"""
1. 计算 1~100 求和
2. 加入分支结构实现1~100之间的偶数求和
3. 使用Python实现1~100之间的偶数求和
"""
# result = 0
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#         result = result + i
#
# print(result)

#
# result = 0
# for i in range(2, 101, 2):
#     print(i)
#     result = result + i
#
# print(result)

# a = 0
# while a < 5: a += 1
# else:
#     print("a >= 5")
#     print(a)

#
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
#
# print("using break done")
#
# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)


# 猜数字

import random

answer = random.randint(1,100)

while True:
    guess = int(input("请输入一个数字:"))
    if guess < answer:
        print("请猜大一点")
    elif guess > answer:
        print("请猜小一点")
    elif guess == answer:
        print("猜对了")
        break
