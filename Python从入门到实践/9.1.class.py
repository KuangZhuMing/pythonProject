# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name #定义属性
#         self.type = cuisine_type #定义属性
#
#     def describe_restaurant(self):
#         print(self.name)
#
#     def open_restaurant(self):
#         print(self.type)
#
# restaurant = Restaurant('中餐',"辣") #生成实例
# restaurant.describe_restaurant() #调用方法
# restaurant.open_restaurant()  #调用方法
#
# restaurant1 = Restaurant('大妈',"不辣")
# restaurant2 = Restaurant('大爷',"辣死")
# restaurant1.describe_restaurant() #调用方法
# restaurant1.open_restaurant()  #调用方法
# restaurant2.describe_restaurant() #调用方法
# restaurant2.open_restaurant()  #调用方法
#
#
#
# class User():
#     def __int__(self,first_name,last_name,*intro):
#         self.fname = first_name
#         self.lname = last_name
#         self.intro = (intro,)
#
#     def describe_user(self):
#         print(self.fname + self.lname + self.intro)
#     def greet_user(self):
#         print("hello")
#
# user1 = User('zhuming','fefe','niubi')
# user1.describe_user()
# user1.greet_user()


# class Car():
#     def __int__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odmeter_reading = 0
#     def get_discriptive(self):
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()
#
# my_new_car = Car('AA','EFE',33)
# print(my_new_car.get_discriptive())

# 9.2使用类和实例
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """将里程表读数设置为指定的值"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            """加一处判断，禁止里程数往后面修改"""
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 1.修改属性的值,直接修改
# my_new_car.odometer_reading = 21
# my_new_car.read_odometer()

# #2.通过方法修改属性的值
# my_new_car.update_odometer(18)
# my_new_car.read_odometer()
#
# # 3. 通过方法对属性的值进行递增
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# 9.3继承
"""super() 是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar 的父类的方法__init__() ，让ElectricCar 实例包含父类的所
有属性。父类也称为超类超 （superclass），名称super因此而得名"""

#将电池类独立出来
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """"打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately" + str(range)



class ElectricCar(Car):
    """继承父类，电动车的独特之处"""

    def __init__(self, make, model, year):
        """ 初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery() #调用另外一个类

# class ElectricCar(Car):
#     """继承父类，电动车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """ 初始化父类的属性，再初始化电动汽车特有的属性"""
#         super().__init__(make, model, year)
#         self.battery = Battery() #调用另外一个类

    #def describe_battery(self):
        #print("This car has a " + str(self.battery_size) + "-kWh battary.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
        #如果父类有这个方法，而且电动车子类还被调用了，提示！！！


my_telas = ElectricCar('tesla', 'model s', 2015)
print(my_telas.get_descriptive_name())



# """Python 2.7中的继承"""Python 2.7中的继承
# class Car(object):
#     def __init__(self, make, model, year):
#         """--snip--"""
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)
# """函数super() 需要两个实参：子类名和对象self 。为帮助Python将父类和子类关联起来，这些实参必不可少。另外，在Python 2.7中使用继承时，务必在定义父类时在括号内指
# 定object 。"""

# 9.3.3 给子类定义属性和方法
# my_telas.describe_battery()
#9.3.4 重写父类的方法
"""只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这
个父类方法，而只关注你在子类中定义的相应方法。如果有人对电动汽车调用方法fill_gas_tank() ，Python将忽略Car 类中的方法fill_gas_tank() ，转而运行上述代码。使用继承时，可让子类保留从父类那里继
承而来的精华，并剔除不需要的糟粕。"""

#9.3.5 将实例用作属性
my_tesla = ElectricCar('gs','4',2016)  #创建一个实例
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()  #在调用battery里面的方法

#9.4 导入类
#from car import Car,ElectricCar,Battery
#导入整个模块
import car
#导入模块中所有的类
#from module_name import *
#9.4.6 在一个模块中导入另一个模块

