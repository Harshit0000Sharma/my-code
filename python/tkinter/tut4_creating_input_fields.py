from tkinter import *

root = Tk()


def label():
    myLabel = Label(root, text="Enter your name")
    myLabel.grid(row=0, column=0)


label()

entry = Entry(root, width=50, bg="white", fg="black")
entry.grid(row=4, column=0)
#! insert() will insert some text at the start of the entry()
# entry.insert(0, "hello")


def button():
    hello = 'Hello '+entry.get()
    myLabel = Label(root, text=hello)
    myLabel.grid(row=11, column=0)


myButton = Button(root, text="enter", padx=50,
                  pady=50, command=button, fg="white", bg="black")

myButton.grid(row=9, column=0)
root.mainloop()
