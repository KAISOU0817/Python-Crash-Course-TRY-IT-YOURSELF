class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Our restaurant '+ self.restaurant_name.title() +' make '+self.cuisine_type.title())
    
    def open_restaurant(self):
        print('We open from 9am to 10pm.\n')


my_restaurant = Restaurant('Panda Ramen','Chinese food')
lily_restaurant = Restaurant('Kura sushi','sushi')
amy_restaurant = Restaurant('KFC','Fried chicken')


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
lily_restaurant.describe_restaurant()
lily_restaurant.open_restaurant()
amy_restaurant.describe_restaurant()
amy_restaurant.open_restaurant()