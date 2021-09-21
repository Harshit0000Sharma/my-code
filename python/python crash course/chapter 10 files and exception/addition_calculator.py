print("Enter 'q' anytime to quit.\n")
while True:
    try:
        num1=input(print("\nenter the first number you want to sum"))
        if num1=="q":
            break
        num1=int(num1)

        num2=input(print("\nenter the second number you want to sum"))
        if num2=="q":
            break
        num2=int(num2)

    except ValueError:
        msg=("you can't enter text for addition")
        print(msg)
    else:
        sum = num1 + num2
        print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))