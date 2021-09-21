from math import pi


class Shape:
    def square():
        try:
            side = input(print("Enter a side of the square"))
            side = float(side)
            s_choice = input(
                print("Enter you want to find area or perimeter of the square"))
            s_choice = s_choice.lower()
            if s_choice == "area":
                print(f"The area of square of side {side} is {side*side}")
            elif s_choice == "perimeter":
                print(f"The perimeter of square of side {side} is  {4*side}")
            else:
                print("you can choose only between area or perimeter")
        except ValueError:
            print("You can only enter  number")

    def circle():
        try:
            radius = input(print("Enter the radius of circel"))
            radius = float(radius)
            c_choice = input(
                print("Enter you want to find area or circunfrance of the circle"))
            c_choice = c_choice.lower()
            if c_choice == "area":
                print(
                    f"The area of circle of radius{radius} is {pi*radius**2}")
            elif c_choice == "circumfrace":
                print(
                    f"The circumfrance of circle radius {radius} is  {2*pi*radius}")
            else:
                print("you can choose only between area or circumfrance")
        except ValueError:
            print("You can only enter  number")

    def rectangle():
        try:
            ab = input(print("Enter the length of side ab in the rectangle"))
            bc = input(print("Enter the length of side ab in the rectangle"))
            cd = input(print("Enter the length of side ab in the rectangle"))
            da = input(print("Enter the length of side ab in the rectangle"))

            ab = float(ab)
            bc = float(bc)
            cd = float(cd)
            da = float(da)

            r_choice = input(
                print("Enter you want to find area or perimeter of the rectangle"))
            r_choice = r_choice.lower()
            if r_choice == "area":
                print(f"The area of rectangle of is {ab*bc}")
            elif r_choice == "perimeter":
                print(f"The perimeter of rectangle of  is  {2*(ab+bc)}")
            else:
                print("you can choose only between area or perimeter")
        except ValueError:
            print("You can only enter  number")


shape = input(print("enter the shape:"))
shape = shape.lower()
a = Shape
if shape == "square":
    a.square()
elif shape == "circle":
    a.circle()
elif shape == "rectangle":
    a.rectangle()
