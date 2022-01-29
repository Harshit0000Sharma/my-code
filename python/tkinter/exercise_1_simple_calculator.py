import tkinter.font as font
from tkinter import *

root = Tk()
myfont = font.Font(size=20)
root.title("Simple Calculator")


def button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    first_number = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first_number)
    e.delete(0, END)


def subtract():
    first_number = e.get()
    global first_num
    global math
    math = "subtract"
    first_num = int(first_number)
    e.delete(0, END)


def divide():
    first_number = e.get()
    global first_num
    global math
    math = "divide"
    first_num = int(first_number)
    e.delete(0, END)


def multiply():
    first_number = e.get()
    global first_num
    global math
    math = "multiply"
    first_num = int(first_number)
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, int(first_num)+int(second_number))
    if math == "subtract":
        e.insert(0, int(first_num)-int(second_number))
    if math == "multiply":
        e.insert(0, int(first_num)*int(second_number))
    if math == "divide":
        e.insert(0, float(first_num) / float(second_number))


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button(0))
button_clear = Button(root, text="C", padx=100, pady=20, command=clear)
button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_equal = Button(root, text="=", padx=100, pady=20, command=equal)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide)
button_exit = Button(root, text="exit", padx=40, pady=20, command=root.quit)

button_1['font'] = myfont
button_2['font'] = myfont
button_3['font'] = myfont
button_4['font'] = myfont
button_5['font'] = myfont
button_6['font'] = myfont
button_7['font'] = myfont
button_8['font'] = myfont
button_9['font'] = myfont
button_0['font'] = myfont
button_add['font'] = myfont
button_multiply['font'] = myfont
button_clear['font'] = myfont
button_subtract['font'] = myfont
button_divide['font'] = myfont
button_equal['font'] = myfont
button_exit['font'] = myfont

# Adding buttons
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_7.grid(row=1, column=0)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_clear.grid(row=4, column=1, columnspan=2)
button_0.grid(row=4, column=0)

button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=5, column=0)

button_add.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)
button_divide.grid(row=6, column=0)
button_exit.grid(row=7, column=0, columnspan=3)

root.mainloop()
