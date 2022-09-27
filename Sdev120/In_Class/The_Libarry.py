#GET VALUE TYPE (CHECKERS)

from operator import ge


def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            print("Please Enter a number.")
            continue

def get_flaot():
    while True:
        try:
            x = float(input("Enter a number: "))
            return x
        except ValueError:
            print("Please Enter a number.")
            continue

def get_str():
    while True:
        try:
            x = input("Enter text: ")
            return x
        except ValueError:
            print("Please enter words.")
            continue


#CLEAR SCREEN
def clear():
    import os
    os.system("cls" if os.name == 'nt' else "clear")

num1 = get_int()
f1= get_flaot()
st= get_str()