menu=('paneer','naan','pizza','ice cream','dal makhni')
for item in menu[:]:
    print('this is our menu '+item)
#menu.pop('naan')not a mistake part of question 

menu_items = (
    'sandwich', 'momos', 'noodles'
    'spring role', 'cutlets','paneer','naan','pizza','ice cream',
    'dal makhni')
print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
        print("- " + item)
