file = ['cat.txt', 'dog.txt']

for file in file:
    
    try:
        with open(file) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + file)
        print(contents)