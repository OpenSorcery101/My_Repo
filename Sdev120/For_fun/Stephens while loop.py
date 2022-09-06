from tkinter import *

root = Tk()
root.title("THE BETTER LOOP!!")

question = ('y')
print(question)

def counter():
    count = 0
    while count < 10:
        count = 1 + count
        count_label= Label(root, text = count)
        count_label.pack(pady=20)

counter()
##MAKEING THIGS APPEAR TO THE SCREEN
statement = Label(root, text = "Would you like to play again?")
statement.pack
myButton = Button(root, text = " y/n ")
myButton.pack()
'''
while question == 'y':
    counter()
    question=input("Would you like to play again? y/n: ")
    if question == 'y':
        question == 'y'
    else:
        question == "n"
'''
mainloop()

