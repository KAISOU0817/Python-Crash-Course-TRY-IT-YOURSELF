age = int(input("请输入一个你的年龄："))

if age < 2:
    print("He is a baby.")
elif age < 4:
    print("He is learning walking.")
elif age < 13:
    print("He is a child.")
elif age < 20:
    print("He is a teenager.")
elif age < 65:
    print("He is an adult.")
else:
    print("He is an elder.")
