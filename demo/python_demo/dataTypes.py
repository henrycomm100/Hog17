print("Hi PyCharm!")
a = 1
print(a)
print(id(a))

int_a = 1
float_a = 0.2
complex_a = 0.2j

print(type(int_a))
print(type(float_a))
print(type(complex_a))

# list 列表
list1 = [1, 2, 3, 4, 5, 6]
print(list1[0])
print(list1[0:5:3])
print(list1[:])

list2 = [1, 2, 3, "a", "b", "c", False, True]
print(list2[2])
print(list2[2:-2])
print(list2[2::2])  # 前闭后开原则， start:stop:step

# string 字符串
str_a = "can you see this?"
str_b = "123"
str_cn = "特殊字符就不需要转义了，比如说这个\r\n表示换行"
str_escape = r"特殊字符就不需要转义了，比如说这个\r\n表示换行"
print(str_a + str_b)
print(str_cn)
print(str_escape)

# string index
var = "abcdefg"
print(var[0])
print(var[1:])
print(var[1:5])  # 前闭后开原则，1 <=x < 5
print(var[1:5:2])  # 步长 start:stop:step
