users=['khudhi','priyanka','umesh','admin','harshit']

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")
        