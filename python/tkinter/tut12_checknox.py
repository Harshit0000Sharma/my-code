from tkinter import *
root = Tk()


def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()


var = StringVar()

button = Checkbutton(root, text="Check this button",
                     variable=var, onvalue="checked", offvalue="unchecked")
button.deselect()
button.pack()
mybutton = Button(root, text="show selection", command=show).pack()
root.mainloop()
