# Python面向对象编程

# 创建一个人的类

class Person:
    # 类 变量
    name = 'default_name'
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # print("init function")
        # 实例 变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # def set_age(cls, age):  # 一般不会写这种方法，类中有__init__方法可以实现这个功能
    #     cls.age = age

    @classmethod  # 类方法需要添加 @classmethod 装饰器
    def born(self):
        print(f"{self.name} is born")

    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")

    def sleep(self):
        print(f"{self.weight} this weight is sleeping")

# jane = Person()
# jane.name = 'Jane Doe'
# jane.age = 30
# jane.gender = 'female'
#
# print(jane.name)
# jane.eat()
# jane.play()
# jane.sleep()


john = Person('John Smith', 50, 'male', 70)
print(john.weight)
john.eat()
# john.set_age(17)
print(f"john's age is {john.age}")

print(f"John's name is {john.name}, John's weight is {john.weight}")

# 类变量和实例变量的区别
print(f"类变量，直接调用，是什么值，{Person.name}")
print(f"实例变量，是什么值，{john.name}")

# 类方法和实例方法的区别
Person.born()  # 类方法需要添加 @classmethod 装饰器，才可以访问
john.eat()
