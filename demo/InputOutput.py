## 字面量插值 literals


name = 'henry'
age = 33
num = 3.14159

# 格式化输出
print("my name is %s, my age is %d, my favorite number is %f, another num is %.2f" % (name, age, num, num))

# str.format()
list1 = [1, 3, 5]
tuple1 = (1, 3, 4, 7)
set1 = {2, 3, 3, 5}
dict1 = {'name': 'henry', 'gender': 'male', 'age': '33'}

print("my name is {} and my age is {}".format(name, age))
print("my name is {0} and my age is {1}".format(name, age))  # same as above
print("my name is {1} and my age is {0}, and again {0}, {1}".format(name, age))  # see the diff

print("my list is {}, dict is {}".format(list1,dict1))

listNames = ['henry','vincent','eric']
print("our names are {}, {} and {}".format(*listNames)) # 列表解包，加*
print("my name is {name}, my gender is {gender}".format(**dict1)) # 列表解包，加*

# F-strings -- 这种最简单，推荐使用
print(f'my name is: \n {name}, my list is {list1}, my age is {age}') # 使用转义字符
print(f'my name is: {name.upper()}, my list length is {len(list1)}, my age is {age}') # 使用函数
print(f"list element is {list1[0]}, dict element is {dict1['gender']}") # 打印列表项，字典项

print(f"result is {(lambda x: x+2)(2)}")