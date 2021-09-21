sandwiches_order=['classic','cheese','veg loaded','omelet']
finished_order=[]
while sandwiches_order:
    current_sandwich=sandwiches_order.pop()
    print("\nI am currently working on your "+current_sandwich.title())
    finished_order.append(sandwiches_order)
print("\n")
for sandwich in current_sandwich:
    print("your "+ current_sandwich+ " is ready")