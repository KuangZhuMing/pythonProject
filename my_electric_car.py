from car import ElectricCar

my_tesla = ElectricCar('tesla','modle s',2022)

print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size=50 #自己定义一个电池容器
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
