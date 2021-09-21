ab=input(print("enter the length of ab: "))
bc=input(print("enter the length of bc: "))
ca=input(print("enter the length of ca: "))

if ab==bc==ca:
    print("equilateral triangle")
else:
    if ab==bc or bc==ca or ca==ab:
        print("isosceles triangle")
    else:
        print("scalene triangle")