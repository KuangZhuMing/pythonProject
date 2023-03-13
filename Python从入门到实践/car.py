"""一个可用于表示汽车的类"""
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

# class Battery():
#     """一次模拟电动汽车电瓶的简单尝试"""
#     def __init__(self, battery_size=60):
#         """初始化电瓶的属性"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """"打印一条消息，指出电瓶的续航里程"""
#         if self.battery_size >= 70:
#             range = 240
#         elif self.battery_size < 70:
#             range = 200
#         elif self.battery_size >= 85:
#             range = 270
#         message = "This car can go approximately " + str(range) + " miles on a full charge."
#         print(message)
#
#     # def get_range(self):
#     #     """"打印一条消息，指出电瓶的续航里程"""
#     #     if self.battery_size == 70:
#     #         range = 240
#     #     elif self.battery_size == 85:
#     #         range = 270
#     #     message = "This car can go approximately" + str(range)
#
# class ElectricCar(Car):
#     """继承父类，电动车的独特之处"""
#     def __init__(self, make, model, year):
#         """ 初始化父类的属性，再初始化电动汽车特有的属性"""
#         super().__init__(make, model, year)
#         self.battery = Battery() #调用电池类

