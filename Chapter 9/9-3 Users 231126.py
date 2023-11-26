class User():


    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def describe_user(self):
         print("username is: " + self.first_name + " "+ self.last_name)
 
    def greet_user(self):
         print("hello, "+self.last_name+'!')

user_1 = User("John","Smith")
user_1.describe_user()
user_1.greet_user()