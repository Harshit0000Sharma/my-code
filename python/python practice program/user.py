def user():
    sum1 = 0
    n = int(input("Please enter number "))
    for i in range(1, n + 1):
        sum1 += i
    print("\n")
    print("Sum is: ", sum1)


user()
