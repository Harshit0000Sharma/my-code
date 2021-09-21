file='programming_poll.txt'

print("Enter 'quit' when you want to stop.")

while True:
    name = input("\nwhy you love programming ? ")
    if name == 'quit':
        break
    else:
        with open(file, 'a') as f:
            f.write(name + "\n")
        