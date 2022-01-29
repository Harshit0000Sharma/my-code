from tkinter import *

root = Tk()


def button():
    myLabel = Label(root, text="you clicked me")
    myLabel.pack()
#! we can also define the state and the size of the button


myButton = Button(root, text="I am a button", padx=50,
                  pady=50, command=button, fg="blue", bg="black")
#myButton = Button(root, text="I am a button",state="enable")
#myButton = Button(root, text="I am a button",state="disable")
myButton.pack()
root.mainloop()
