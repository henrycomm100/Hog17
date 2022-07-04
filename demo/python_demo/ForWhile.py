"""
1. 计算 1~100 求和
2. 加入分支结构实现1~100之间的偶数求和
3. 使用Python实现1~100之间的偶数求和
"""

# 0 -100 求和
result = 0
for i in range(101):
    print(i)
    result = result + i

print(result)

# 0-100 偶数求和 - 使用分支结构
result = 0
for i in range(101):
    if i % 2 == 0:
        print(i)
        result = result + i

print(result)

# 0-100 偶数求和
result = 0
for i in range(2, 101, 2):
    print(i)
    result = result + i

print(result)

# while 循环
a = 0
while a < 5:
    a += 1
else:
    print("a >= 5")
    print(a)

# break 跳出 for和while循环体。任何对应的循环else块将不再执行
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("using break done")

# continue - 调过当前循环块的剩余语句，然后继续进行下一轮循环
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# 猜数字

import random

answer = random.randint(1, 100)

while True:
    guess = int(input("请输入一个数字:"))  # 需要将输入的数字转换为int
    if guess < answer:
        print("请猜大一点")
    elif guess > answer:
        print("请猜小一点")
    elif guess == answer:
        print("猜对了")
        break
