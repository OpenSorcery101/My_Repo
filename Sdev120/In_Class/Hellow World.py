from tkinter import *

root = Tk()
root.title("HW!")

window_height = 200
window_width = 200

root.geometry(f"{int(window_height)}x{int(window_width)}")

Words= Label(root,  text=f"Hello  World!")
Words.pack(pady=90)


root.mainloop()