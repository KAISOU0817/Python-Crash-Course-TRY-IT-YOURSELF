rivers = {'nile': 'egypt', 'amazon river': 'bizarre', 'yangtze river': 'china'}

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())