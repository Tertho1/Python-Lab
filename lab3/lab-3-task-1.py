def make_album(artist, title, num_songs=None):
    album = {"artist": artist, "title": title}
    if num_songs:
        album["num_songs"] = num_songs
    return album

album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide", 16)
album3 = make_album("The Beatles", "Abbey Road")


print(album1)
print(album2)
print(album3)
