from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
#! important note : when coping path it will have "\" you will have to change it to "/"


def open():
    global IMG
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/Harshit/Desktop/gallery",
                                               title="Select file", filetypes=(("jpg file", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.pack()
    IMG = ImageTk.PhotoImage(Image.open(root.filename))
    label_img = Label(image=IMG)
    label_img.pack()


my_button = Button(root, text="open", command=open).pack()
root.mainloop()
