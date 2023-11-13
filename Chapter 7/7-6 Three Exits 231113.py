# #1：use while and if
prompt = "Please tell me a series of pizza ingredients(enter 'quit' to end): "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("We'll add " + message + " into your pizza.")

'''#2:use active
active = True
prompt = "Please tell me a series of pizza ingredients(enter 'quit' to end): "
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        # print("That's all! Please wait ten minutes.")
    else:
        print("We'll add " + message + " into your pizza.")
'''

'''#3:use break
prompt = "Please tell me a series of pizza ingredients(enter 'quit' to end): "
while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print("We'll add " + message + " into your pizza.")
'''
