vehicle = ['car','motorcycle','ship','bike']
messages = ' I would like to own a '
for i in vehicle:
    print (messages + i +'.')


# array.append() can add elements to the end of the list
# array.insert(num,'xxx')

vehicle.insert(2,'sports car')
for i in vehicle:
    print (i)


# use  'del array[num]' to delete elements
# list can think as a stack
# array.pop(num)
# array.remove ('xxx')