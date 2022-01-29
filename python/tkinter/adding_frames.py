from tkinter import *
from PIL import ImageTk, Image

root = Tk()
frame = LabelFrame(root, text="Frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)
button = Button(frame, text="exit this GUI already!!")
button.pack()
root.mainloop()
