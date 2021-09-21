# question 8-13
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'q' at any time to stop.")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break
    
    title = input(title_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")