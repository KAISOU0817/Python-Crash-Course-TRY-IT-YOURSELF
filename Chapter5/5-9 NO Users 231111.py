users = ['AOKI', 'Jack', 'Alice', "Mike", "Tom", 'admin']

users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some users!")