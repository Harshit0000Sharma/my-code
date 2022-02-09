from tkinter import *

root = Tk()


def open():
    new_window = Toplevel()


Button(root, text="Open second window", command=lambda: open()).pack()
root.mainloop()
