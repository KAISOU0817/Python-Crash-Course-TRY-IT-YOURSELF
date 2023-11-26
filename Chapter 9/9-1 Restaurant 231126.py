# class MyClass:
#     def instance_method(self):
#         return "This is an instance method."

#     def another_method(self, value):
#         return f"Another method with value: {value}"

# # 创建类的实例
# my_instance = MyClass()

# # 调用实例方法
# result1 = my_instance.instance_method()
# result2 = my_instance.another_method("Hello
# print(result1)
# print(result2)


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Our restaurant '+ self.restaurant_name.title() +' make '+self.cuisine_type.title())
    
    def open_restaurant(self):
        print('We open from 9am to 10pm.')

my_restaurant = Restaurant('Panda Ramen','Chinese food')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
