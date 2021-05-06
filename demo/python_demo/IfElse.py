# 分支结构
x = -2
if x > 1:
    y = 3*x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5*x + 3

print(y)

#多重分支
x = -2
if x > 1:
    y = 3*x -5
elif -1 <= x < 1:
    y = x + 2
elif x < -1:
    y = 5*x + 3

print(y)