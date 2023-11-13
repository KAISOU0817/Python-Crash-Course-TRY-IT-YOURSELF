responses = {}
active = True
while active:
    name = input("What is your name?")
    place = input("If you could visit one place in the world, where would you go?")

    responses[name] = place

    repeat = input("Enter 'quit' when you finished ")
    if repeat == 'quit':
        active = False

print("--- Results ---")
for name, place in responses.items():
    print(name + "'s dream resort is " + place)