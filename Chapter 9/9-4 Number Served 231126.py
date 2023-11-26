class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Our restaurant '+ self.restaurant_name.title() +' make '+self.cuisine_type.title())
    
    def open_restaurant(self):
        print('We open from 9am to 10pm.')
    
    def set_number_served(self,num):
        self.number_served=num


my_restaurant = Restaurant('Panda Ramen','Chinese food')
print('there are already '+str(my_restaurant.number_served) +' people been here')

my_restaurant.set_number_served(100)
print('there are already '+str(my_restaurant.number_served) +' people been here')