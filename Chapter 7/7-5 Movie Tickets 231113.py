while True:
    message = input('How old are you?')

    if message =='quit':
        break
    else:
        age = int(message)
        if age <3:
            print('You are free.')
        elif age<12:
            print('You should pay 10 dollars.')
        else:
            print('You should pat 15 dollars.')