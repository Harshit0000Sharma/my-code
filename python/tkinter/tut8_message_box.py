from tkinter import *
from tkinter import messagebox

root = Tk()


def open():
    messagebox.showinfo(
        "message box", "this message box is created by harshit")
    messagebox.askquestion(
        "message box", "this message box is created by harshit")
    messagebox.showwarning(
        "message box", "this message box is created by harshit")
    messagebox.showerror(
        "message box", "this message box is created by harshit")
    messagebox.askokcancel(
        "message box", "this message box is created by harshit")
    messagebox.askyesno(
        "message box", "this message box is created by harshit")


Button(root, text="open", command=lambda: open()).pack()
root.mainloop()
