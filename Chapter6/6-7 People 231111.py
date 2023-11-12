wangxiaoming = {'first_name':'xiaoming','last_name':'wa','age':21,'city':'kyoto'}
zhangsan = {'first_name':'san','last_name':'zhang','age':21,'city':'tokyo'}
lisi = {'first_name':'si','last_name':'li','age':22,'city':'beijing'}
people = [wangxiaoming,zhangsan,lisi]

for person in people:
    name = person['last_name'] + person['first_name']
    print("Name: " + name)
    print("Age: " + str(person['age']))
    print("City: " + person['city'])