magicians=['Jobs','Alice','Joker']
great=[]

def show_magicians(names,great):
    while names:
        add_great=names.pop()
        print(add_great+" is a magician.")
        great.append(add_great)

def make_great(names,great):
    for i in great:
        print('the great '+i)
    names.append(great)
    

show_magicians(magicians,great)
make_great(magicians,great)

print(magicians)