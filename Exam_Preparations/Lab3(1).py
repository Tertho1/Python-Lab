def make_album(artist_name, album_title, number_of_songs=None):
    album = {artist_name: album_title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


print(make_album("Taylor Swift", "1989", 3))
for i in range(3):
    name = input("Enter Artist Name : ")
    title = input("Enter Album Title : ")
    print(make_album(name, title))
