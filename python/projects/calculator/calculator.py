""" Calculator
              by Mr Harshit Sharma
"""


def addition():

    print("Addition")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


print("")


# This function subtracts two numbers
def subtract(x, y):
    return x - y


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]


while True:
    list = []
    print(" Simple Calculator in python by Mr Harshit Sharma")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    c = c.lower()
    if c != 'q':
        if c == 'a':
            try:
                list = addition()
                print("Ans = ", list[0], " total inputs ", list[1])
            except:
                print("an unknown error ocurred ! pls try again")
        elif c == 's':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1, "-", num2, "=", subtract(num1, num2))
            except:
                print("an unknown error ocurred ! pls try again")
        elif c == 'm':
            try:
                list = multiplication()
                print("Ans = ", list[0], " total inputs ", list[1])
            except:
                print("an unknown error ocurred ! pls try again")
        elif c == 'v':
            try:
                list = average()
                print("Ans = ", list[0], " total inputs ", list[1])
            except:
                print("an unknown error ocurred ! pls try again")
        else:
            print("Sorry, invilid character")
    else:
        break
