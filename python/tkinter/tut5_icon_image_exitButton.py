from tkinter import *

#! we use PIL library to use images in tkinter
from PIL import Image, ImageTk

root = Tk()
#!icon
#!👇👇we can pass the location of the .ico file in iconbitmap function
root.iconbitmap("icon.ico")

#!exit button
exit = Button(root, text="Exit", command=root.quit)
exit.pack()

#! using images
IMG = ImageTk.PhotoImage(Image.open("image.jpg"))
label = Label(image=IMG)
label.pack()

root.mainloop()
