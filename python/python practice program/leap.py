year=int(input(print("enter the year")))
if year % 4 == 0:
    print("leap year")
    if year % 100 == 0 and year%400!=0:
        print("not a leap year")
