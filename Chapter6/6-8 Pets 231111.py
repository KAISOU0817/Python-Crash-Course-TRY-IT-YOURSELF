milly = {'name':'milly','variety': 'cat', 'owner_name': 'Amy'}
spike = {'name':'spike','variety': 'dog', 'owner_name': 'John'}
dodo = {'name':'dodo','variety': 'bird', 'owner_name': 'Mike'}
pets = [milly,spike,dodo]

for pet in pets:
    print("Name: " + pet['name'])
    print("Variety: " + pet['variety'])
    print("Owner name: " + pet['owner_name'])