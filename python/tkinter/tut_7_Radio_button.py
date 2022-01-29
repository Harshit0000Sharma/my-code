from tkinter import *
from PIL import ImageTk, Image

root = Tk()
r = IntVar()
r.set("2")


def clicked(value):
    lavel = Label(root, text=value)
    lavel.pack()


Radiobutton(root, text="Radiobutton 1", variable=r, value=1,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Radiobutton 2", variable=r, value=2,
            command=lambda: clicked(r.get())).pack()

lavel = Label(root, text=r.get())
lavel.pack()

root.mainloop()
