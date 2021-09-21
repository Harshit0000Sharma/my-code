name=input(print("what's your name: "))
with open("guest.txt","a") as f:
    f.write("\n"+name)