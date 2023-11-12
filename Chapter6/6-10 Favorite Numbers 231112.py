numbers = {'AOKI':[1,3], 'Jack':[8,7], 'Alice':[6,9,11], "Mike":[5], "Tom":[5,8]}
for name,number in numbers.items():
    print (name + "'s favorite number is ")
    for num in number:
        print(num)