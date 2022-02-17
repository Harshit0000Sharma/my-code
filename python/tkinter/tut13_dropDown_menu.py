from tkinter import *
root = Tk()


def show():
    myButton = Label(root, text=clicked.get())
    myButton.pack()


option = ["monday",
          "tuesday",
          "wednesday",
          "thursday",
          "friday",
          "saturday",
          "sunday"]

clicked = StringVar()
clicked.set(option[0])
# dropdown menu
drop = OptionMenu(root, clicked, *option)
drop.pack()
button = Button(root, text="show selection", command=show)
button.pack()
root.mainloop()
