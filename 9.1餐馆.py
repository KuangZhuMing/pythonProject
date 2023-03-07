class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name #定义属性
        self.type = cuisine_type #定义属性

    def describe_restaurant(self):
        print(self.name)

    def open_restaurant(self):
        print(self.type)

restaurant = Restaurant('中餐',"辣") #生成实例
restaurant.describe_restaurant() #调用方法
restaurant.open_restaurant()  #调用方法

restaurant1 = Restaurant('大妈',"不辣")
restaurant2 = Restaurant('大爷',"辣死")
restaurant1.describe_restaurant() #调用方法
restaurant1.open_restaurant()  #调用方法
restaurant2.describe_restaurant() #调用方法
restaurant2.open_restaurant()  #调用方法



class User():
    def __int__(self,first_name,last_name,*intro):
        self.fname = first_name
        self.lname = last_name
        self.intro = (intro,)

    def describe_user(self):
        print(self.fname + self.lname + self.intro)
    def greet_user(self):
        print("hello")

user1 = User('zhuming','fefe','niubi')
user1.describe_user()
user1.greet_user()






