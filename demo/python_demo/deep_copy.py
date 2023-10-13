import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值，传对象的引用

c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
print('type(a) = ', type(a))
print('type(d) = ', type(d))



dict_a = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
dict_b = dict_a
dict_c =copy.copy(dict_a)
dict_d = copy.deepcopy(dict_a)

dict_a["a"] = 55555

print('dict_a = ', dict_a)
print('dict_b = ', dict_b)
print('dict_c = ', dict_c)
print('dict_d = ', dict_d)
print('type(dict_a) = ', type(dict_a))
print('type(dict_d) = ', type(dict_d))