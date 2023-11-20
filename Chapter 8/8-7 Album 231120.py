def make_album(singer,album_name,number=''):
    if number:
        album={'singer name:':singer, 'album:':album_name,'number:':number}
    else:
        album={'singer name:':singer, 'album:':album_name}
    return album

print(make_album('Alice','Hope','5'))
print(make_album('Jerk','Love'))