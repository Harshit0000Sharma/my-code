people = []

person = {
    'first_name': 'umesh',
    'last_name': 'sharma',
    'age': 46,
    'city': 'meerut',
    }
people.append(person)

person = {
    'first_name': 'priyanka',
    'last_name': 'sharma',
    'age': 36,
    'city': 'meerut',
    }
people.append(person)

person = {
    'first_name': 'khushi',
    'last_name': 'sharma',
    'age': 10,
    'city': 'meerut',
    }
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")
