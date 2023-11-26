class User():


    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0

    
    def describe_user(self):
        print("username is: " + self.first_name + " "+ self.last_name)
 
    def greet_user(self):
        print("hello, "+self.last_name+'!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User("John","Smith")
user_1.describe_user()
user_1.greet_user()

print("  Login attempts: " + str(user_1.login_attempts))
user_1.increment_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))
user_1.increment_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))
user_1.increment_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))

user_1.reset_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))