"""
分段函数求值
3x -5 (x>1)
x + 2 (-1<= x <= 1)
5x+3 (x<-1)
"""

# 分支结构 + 分支嵌套
x = -2
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3

print(y)

# 多重分支
x = -2
if x > 1:
    y = 3 * x - 5
elif -1 <= x < 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3

print(y)

# 上面两种方式，哪一种更好呢？
# 扁平化的会比嵌套式的更好 Flat is better than nested. 能使用扁平化的时候，就不要使用嵌套式的。
