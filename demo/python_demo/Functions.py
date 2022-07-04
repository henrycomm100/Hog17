def func1(a=1, b=2, c=3):
    """
    :param a: 定义了默认值为1
    :param b:
    :param c:
    :return:
    """
    print(a)
    print(b)
    print(c)
    return a + b + c


#
# print(func1(2, 3, 4))
#
# print(func1(a=11, b=22, c=33))

print(func1(333, 444))  # 没有传入c，会使用默认值3
print(func1())

print(func1(3, 4, c=5))

# Python 匿名函数(Lambda)
# 用法： lambda arguments: expression

double = lambda x: x * 2
add_result = lambda x, y: x + y
print('lambda表达式返回', double(3))
print('lambda表达式2返回', add_result(3, 4))
