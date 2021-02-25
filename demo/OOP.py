# Python面向对象编程

# 创建一个人的类

class Person:
    # 类 变量
    name = 'default'
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

    @classmethod
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

print(f"John's name is {john.name}, John's weight is {john.weight}")

# 类变量和实例变量的区别
print(Person.name)
print(john.name)

# 类方法和实例方法的区别
Person.born()
john.eat()