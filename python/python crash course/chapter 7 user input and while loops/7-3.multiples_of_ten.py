number=input(print("\ntype a number to weather it is a multiple of 10"))
number=int(number)
if number % 10 ==0:
    print(str(number)+" is a multiple of 10")
elif number%10!=1:
    print(str(number)+ " is not a multiple of 10")