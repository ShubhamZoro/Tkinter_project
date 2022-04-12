from tkinter import *

from PIL import ImageTk,Image
from tkinter import messagebox
i=0
def back():
    global i
    if i>0:
        i=i-1
    else:
        messagebox.showinfo("Alert","Press forward button")

    lable.configure(image=img_list[i])
    status.configure(text=f"Image {i+1} of {len(img_list)}")

def forward():
    global i
    if i<len(img_list)-1:
        i=i+1
    else:
        messagebox.showinfo("Alert", "Press back button")
    lable.configure(image=img_list[i])
    status.configure(text=f"Image {i+1} of {len(img_list)}")

def Quit():
    window.destroy()
window=Tk()
window.title("Image viewer")
img1=ImageTk.PhotoImage(Image.open("images/app-development-banner_33099-1720-modified.png"))
img2=ImageTk.PhotoImage(Image.open("images/cloud.png"))
img3=ImageTk.PhotoImage(Image.open("images/maxresdefault-modified.png"))
img4=ImageTk.PhotoImage(Image.open("images/mountain.png"))


img_list=[img1,img2,img3,img4]

lable=Label(image=img_list[0])
lable.grid(row=0,column=0,columnspan=3)

status=Label(text=f"Image {i+1} of {len(img_list)}")
status.grid(row=2,column=2)

back_button=Button(text="<<",command=back)
exit_button=Button(text="Exit",command=Quit)
forward_button=Button(text=">>",command=forward)

back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
forward_button.grid(row=1,column=2)
window.mainloop()