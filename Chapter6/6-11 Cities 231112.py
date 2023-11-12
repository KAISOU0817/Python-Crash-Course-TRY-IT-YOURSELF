cities = {
    'beijing': {
        'country': 'china',
        'population': '2188.6万',
        'fact': 'Beijing is reduced urban development and large-scale ecological construction have shown the world a high-quality green and livable city.'
    },

    'paris': {
        'country': 'french',
        'population': '224万',
        'fact': "The Paris metropolitan area has a population of about 11 million, accounting for one-sixth of the country's population."
    },

    'tokyo': {
        'country': 'japan',
        'population': '1350万',
        'fact': 'Tokyo is the capital of Japan, located in the middle of the Kanto Plain of Japan.'
    },
}

for city_name, city_info in cities.items():
    print("City name: " + city_name)
    print("population: " + city_info['population'])
    print("fact: " + city_info['fact'])
