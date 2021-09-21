favourite_pizzas = ['peppy paneer', 'veg extravaganza',
                    'farmhouse', 'double cheese margherita', 'capsicum']
for pizzas in favourite_pizzas:
    print(pizzas)
for pizzas in favourite_pizzas:
    print("I really like "+pizzas + " pizza")
print("i really love pizzaz")
# question 4-10 👇👇
print('first 3 item of lists are:')
for pizzas in favourite_pizzas[0:3]:
    print(pizzas)
print('last 3 item of lists are:')
for pizzas in favourite_pizzas[3:7]:
    print(pizzas)
# question 4-11 👇👇
favourite_pizzas = ['peppy paneer', 'veg extravaganza',
                    'farmhouse', 'double cheese margherita', 'capsicum']
friend_pizzas = ['peppy paneer', 'veg extravaganza',
                 'farmhouse', 'double cheese margherita', 'capsicum']
friend_pizzas.append('onion')
print(friend_pizzas)
print(favourite_pizzas)
