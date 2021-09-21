num1=input(print("\nenter the first number you want to sum"))
num2=input(print("\nenter the second number you want to sum"))
try:
    print(int(num1)+int(num2))
except ValueError:
    msg=("you can't enter text for addition")
    print(msg)
