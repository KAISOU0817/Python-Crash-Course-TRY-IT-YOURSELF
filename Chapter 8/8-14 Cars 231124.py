def car_info(manu,number,**info):
    cars_info={'made from':manu,'number':number}
    for key, value in info.items():
        cars_info[key]=value
    return cars_info

aa=car_info('BMW','x5',color='white',old="7years")
print(aa)