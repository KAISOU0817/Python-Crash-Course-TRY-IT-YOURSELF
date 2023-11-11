current_users = ['AOKI', 'Jack', 'Alice', "Mike", "Tom", 'admin']
new_users = ['Jobs','Jack','Cook','JAY','Musk']
for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()
for i in range(len(new_users)):
    new_users[i] = new_users[i].lower()


for user in new_users:
    if user in current_users:
        print("This name has been used,please use other name.")
    else:
        print('This name is avaliable.')