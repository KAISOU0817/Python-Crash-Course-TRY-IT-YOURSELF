names = ['Elon Musk', 'Jobs', 'Euler', "Einstein"]
invite_message =  "! Would you like to have a dinner with me?"
for i in names:
    print("Hi, " + i + invite_message)

print("Sorry to hear that Jobs do not have spare time.")

names[1] = 'Cook'
for i in names:
    print("Hi, " + i + invite_message)
