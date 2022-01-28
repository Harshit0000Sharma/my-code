from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")

my_img1 = ImageTk.PhotoImage(Image.open("tour_1/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("tour_1/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("tour_1/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("tour_1/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("tour_1/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("tour_1/6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("tour_1/7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("tour_1/8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("tour_1/9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("tour_1/10.jpg"))
my_img11 = ImageTk.PhotoImage(Image.open("tour_1/11.jpg"))
my_img12 = ImageTk.PhotoImage(Image.open("tour_1/12.jpg"))
my_img13 = ImageTk.PhotoImage(Image.open("tour_1/13.jpg"))
my_img14 = ImageTk.PhotoImage(Image.open("tour_1/14.jpg"))

IMG_LIST = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7,
            my_img8, my_img9, my_img10, my_img11, my_img12, my_img13, my_img14]

status = Label(root, text="Image 1 out of "+str(len(IMG_LIST)),
               bd=1, relief=SUNKEN, anchor=E)

img_label = Label(image=my_img1)
img_label.grid(row=2, column=0, columnspan=3)


def forward(image_number):
    global img_label
    global button_forward
    global button_back

    img_label.grid_forget()
    img_label = Label(image=IMG_LIST[image_number-1])
    button_forward = Button(
        root, text=">>>", command=lambda: forward(image_number+1))
    button_back = Button(
        root, text="<<<", command=lambda: back(image_number-1))

    if image_number == 14:
        button_forward = Button(root, text=">>>", state=DISABLED)
    img_label.grid(row=2, column=0, columnspan=3)
    button_forward.grid(row=0, column=2)
    button_back.grid(row=0, column=0)

    status = Label(root, text="Image "+str(image_number)+" out of "+str(len(IMG_LIST)),
                   bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=1, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global img_label
    global button_forward
    global button_back

    img_label.grid_forget()
    img_label = Label(image=IMG_LIST[image_number-1])
    button_forward = Button(
        root, text=">>>", command=lambda: forward(image_number+1))
    button_back = Button(
        root, text="<<<", command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<<", state=DISABLED)

    img_label.grid(row=2, column=0, columnspan=3)
    button_forward.grid(row=0, column=2)
    button_back.grid(row=0, column=0)

    status = Label(root, text="Image "+str(image_number)+" out of "+str(len(IMG_LIST)),
                   bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=1, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<<", command=lambda: back())
button_forward = Button(root, text=">>>", command=lambda: forward(2))
button_exit = Button(root, text="exit", command=root.quit)

button_exit.grid(row=0, column=1)
button_forward.grid(row=0, column=2, pady=10)
button_back.grid(row=0, column=0)
status.grid(row=1, column=0, columnspan=3, sticky=W+E)

root.mainloop()
