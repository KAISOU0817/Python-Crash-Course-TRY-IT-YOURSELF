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