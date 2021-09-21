# question 8-7
def make_album(artist,title):
    album_dict={
        "artist": artist.title(),
        "title": title.title()
    }
    return album_dict

album=make_album('rustage','naruto')
print(album)    

album=make_album('da real insane','death note')
print(album)

album=make_album('shawadi','no particular album')
print(album)