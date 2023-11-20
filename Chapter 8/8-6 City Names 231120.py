def city_country(city,country):
    cc=city +', '+country
    return cc.title()

xyz=city_country('beijing','china')
print(xyz)

print(city_country('new york', 'america'))
print(city_country('tokyo', 'japan'))