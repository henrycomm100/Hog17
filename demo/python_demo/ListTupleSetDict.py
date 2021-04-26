# List
# list1 = [1, 3, 2, 5, 7]
# list1.append(9)
# list1.append(1)
# list1.append(0)
#
# list1.insert(1,8)
# list1.remove(5)
#
#
# y = list1.pop(0)
# print(y)
#
# print(list1)
# list1.sort()
# list1.sort(reverse=True)
#
# list1.reverse()
# print(list1)

#
# list_square = []
# for i in range(1, 4):
#     list_square.append(i ** 2)
# print(list_square)
#
# # 列表推导式 list comprehensions
# list_square2 = [i ** 2 for i in range(1, 4)]
# print("list_square2:", list_square2)
#
# list_square3 = [i ** 2 for i in range(1, 4) if i != 1]
# # for i in range(1,4):
# #     if i != 1:
# #         list_square3.append(i**2)
# print("list_square3:", list_square3)

# 嵌套循环
# list_square4 = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         list_square4.append(i * j)
#
# print(list_square4)
#
# list_square5 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_square5)


# 元组 tuple
#
# tuple1 = (1,2,3)
# print(tuple1)
# print(tuple1.count(1))
# print(tuple1.count("a"))
# print(tuple1.index(2))
#
# tuple2 = 'a', 'b', 'c'
# print(tuple2)
# print(type(tuple2))
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# nestedTuple1 = (('a','b','c'), 2, 3)
# tupleWithList = ([1,2,3],[4,5,6])
#
# a = [7,8,9]
# tupleWithList2 = (1,2,a)
# print(id(tupleWithList2[2]))
#
# tupleWithList2[2][0] = 666
# print(id(tupleWithList2[2]))
#
# print(tupleWithList2)


# 集合 set
#
# a = {1}
# b = set()
#
# print(type(a))
# print(type(b))

a = {1,2,3,4}
b = {4,9,7}
# print(a.union(b))
# a.remove(3)
# print(a)
#
# a.add(6)
# print(a)
# c = a.copy()
# print(c)
#
# print(a.difference(b))
print(a.intersection(b))

c ="aslfjdalshfoawhefasd"
print(set(c))


# 字典 Dictionary
dict1 = {"a":1, "b": 2}
dict2 = dict(a=1,b=2)

# print(dict1)
# print(type(dict1))
# print(dict2)
# print(type(dict2))

print(dict1.keys())
print(dict1.values())

print(dict1.pop("a"))
print(dict1)