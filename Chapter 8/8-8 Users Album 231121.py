def make_album(singer,album_name,number=''):
    if number:
        album={'singer name:':singer, 'album:':album_name,'number:':number}
    else:
        album={'singer name:':singer, 'album:':album_name}
    return album

albums=[]
while True:
    print("Please tell me your favorite albums:"+"enter 'quit' to end the program")

    singer_name = input("Singer name: ")
    if singer_name == 'quit':
        break

    album_name = input("Album name: ")
    if album_name == 'quit':
        break

    sign = input("\nDo you know how many songs in this album (yes/no): ")
    if sign == 'yes':
        number = input("Number of songs: ")
        number = int(number)
        album = make_album(singer_name, album_name, number)
        albums.append(album)
    else:
        print("Do not worry! It does not matter")
        album = make_album(singer_name, album_name)
        albums.append(album)

    print("\nLet's check the album:")
    print(album)