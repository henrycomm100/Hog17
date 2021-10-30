# num = 1
# print(name)
#
# list_number = [1, 2, 3]
# print(list_number[0])
# print(list_number[3])

# dict = {"name": "henry"}
# print(dict['name'])


# print(dict['age'])
#
# num = input("please input a number: ")
# print(int(num))


def divide(a, b):
    return a / b


divide(4, 2)
# divide(4, 0)
try:
    res = divide(4, 2)
    list_number = [1, 2, 3]
    # print(list_number[3])
except Exception as e:
    print(e)
    print("这里出现了一个异常")
else:
    print("没有异常时会执行")
    print(res)
finally:
    print("不管是否有异常都会执行")
    # print(res)


class MyException(Exception):
    def __init__(self, msg):
        print(f"这里有一个自定义的异常: {msg}")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"你输入的值{num}不合法，请重新输入")
    else:
        print(f"你设置了年龄为：{num}")


set_age(10)
set_age(0)
