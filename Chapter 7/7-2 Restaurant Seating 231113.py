message = input('How many people?')
message =int(message)
if message <= 8:
    print('We have availability.')
else:
    print('We have no open seats.')