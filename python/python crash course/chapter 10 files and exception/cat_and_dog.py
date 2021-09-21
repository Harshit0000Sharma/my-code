file = ['cat.txt', 'dog.txt']

for file in file:
    print("\nReading file: " + file)
    try:
        with open(file) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")