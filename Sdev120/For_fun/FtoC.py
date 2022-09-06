
from pydoc import describe
from tkinter import *

root = Tk()
root.title("Whats the temprature?")
def Fmodule():
    putin = Entry(root, width= 100)
    putin.pack()
    Fahrenheit = Label(root, text="What themprature is it in Fahrenheit? : ")
    Fahrenheit.pack()

    Fentry = Entry(root, width=25)
    Fentry.pack()
    fCelsuis = Fentry.get

    fCelsuis = float(float(Fahrenheit)-32)* 5/9
    fCelFinalnum = round(fCelsuis,1)
    FFinal= Label(root, text = str(Fahrenheit) +" Fahrenheit is " + str(fCelFinalnum) + " in Celsius")


def Cmoduel():
    Celsius = input("What themprature is it in Celsius? : ")
    cFahrenheit = float(float(Celsius)*9/5) + 32
    cFahFinalnum = round(cFahrenheit,1)
    print(str(Celsius) +" Celsius is " + str(cFahFinalnum) + " in Fahrenheit")


def decide():
    desision= putin.get
    if desision == "1":
        Fmodule()
    elif desision == "2":
        Cmoduel()

def enter():
    Hello = "Hello" + putin.get()
    decide()


choice = Label(root, text= "Enter 1 or 2] 1.)Fahrenheit to Celsius, or 2.) Celsius to Fahrenheit:")
choice.pack(pady=10)

putin = Entry(root, width= 100)
putin.pack()

button = Button(root, text ="Enter", command=enter)
button.pack()



'''
choice = input ("Press 1 / 2 | 1.)Fahrenheit to Celsius, or 2.) Celsius to Fahrenheit: ")


Verify= int(choice)

if Verify == 1:
    Fahrenheit = input("What themprature is it in Fahrenheit? : ")
    fCelsuis = float(float(Fahrenheit)-32)* 5/9
    fCelFinalnum = round(fCelsuis,1)
    print(str(Fahrenheit) +" Fahrenheit is " + str(fCelFinalnum) + " in Celsius")
elif Verify ==2:
    Celsius = input("What themprature is it in Celsius? : ")
    cFahrenheit = float(float(Celsius)*9/5) + 32
    cFahFinalnum = round(cFahrenheit,1)
    print(str(Celsius) +" Celsius is " + str(cFahFinalnum) + " in Fahrenheit")
else:
    print("That is not an option please try again!")
'''
mainloop()





'''
#Choice
choice = input ("Press 1 / 2 | 1.)Fahrenheit to Celsius, or 2.) Celsius to Fahrenheit: ")


Verify= int(choice)

if Verify == 1:
    Fahrenheit = input("What themprature is it in Fahrenheit? : ")
    fCelsuis = float(float(Fahrenheit)-32)* 5/9
    fCelFinalnum = round(fCelsuis,1)
    print(str(Fahrenheit) +" Fahrenheit is " + str(fCelFinalnum) + " in Celsius")
elif Verify ==2:
    Celsius = input("What themprature is it in Celsius? : ")
    cFahrenheit = float(float(Celsius)*9/5) + 32
    cFahFinalnum = round(cFahrenheit,1)
    print(str(Celsius) +" Celsius is " + str(cFahFinalnum) + " in Fahrenheit")
else:
    print("That is not an option please try again!")
    '''




