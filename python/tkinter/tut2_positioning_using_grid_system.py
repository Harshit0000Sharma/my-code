from tkinter import *


root = Tk()


def label():
    myLabel = Label(root, text="yo,I am Harshit")
    myLabel.grid(row=1, column=0)
    myLabel1 = Label(root, text="hello")
    myLabel1.grid(row=0, column=0)
    root.mainloop()


#! difference between pack() and grid() that grid() creats a immovable widget

# myLabel.grid(row=1, column=0)
# myLabel1.grid(row=0, column=0)
label()
