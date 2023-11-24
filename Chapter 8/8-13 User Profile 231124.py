def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}

    for key, value in user_info.items():
        profile[key] = value

    return profile


my_profile = build_profile('San', 'Zhang', height='180cm', weight='64kg', locaton='shanghai')
print(my_profile)