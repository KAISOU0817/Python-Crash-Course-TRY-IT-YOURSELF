names = ['Elon Musk', 'Cook', 'Euler', "Einstein"]
invite_message =  "! Would you like to have a dinner with me?"
for i in names:
    print("Hi, " + i + invite_message)

print("I bought a bigger table, so I can invite 3 guests additionally.")

names.insert(0,'Jack Ma')
names.insert(2,'Trump')
names.append('Taylor')
for i in names:
    print("Hi, " + i + invite_message)

print("Oh no! I just learned that the newly purchased table could not be delivered in time, so I can only invite 2 "
      "guests.")

while len(names) > 2:
    popped_guest = names.pop()
    notice_message = "I'm sorry, " + popped_guest + ". I can't invite you to dinner."
    print(notice_message)

for i in names:
    print("Hi, " + i + ",you are still invited")

print ('I have ' + str(len(names)) + ' dinners')