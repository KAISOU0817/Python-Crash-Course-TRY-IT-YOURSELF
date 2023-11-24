magicians=['Jobs','Alice','Joker']
great=[]

def show_magicians(names,great):
    while names:
        add_great=names.pop()
        print(add_great+" is a magician.")
        great.append(add_great)

def make_great(great):
    for i in great:
        print('the great '+i)
    
magicians=['Jobs','Alice','Joker']
great=[]
show_magicians(magicians,great)
make_great(great)
