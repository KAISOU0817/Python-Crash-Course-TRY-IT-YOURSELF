favorite_places = {
    'Mite': ['kyoto', 'tokyo'], 'Job': ['Nanjing'], 'Musk': ['Shanghai']
    }
for name,places in favorite_places.items():
    if len(places) == 1:
         print(name + "'s favorite place is: ")
         for place in places:
           print(place)
    else:
         print(name + "'s favorite places are: ")
         for place in places:
             print(place)