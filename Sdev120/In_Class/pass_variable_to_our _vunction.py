import os

def clear():
    os.system('cls' if os.name =='nt' else "clear")

def get_num(quetion):
    while True:
        try:
            x = int(input(quetion))
            return x
        except ValueError:
            print("This is not a number")
            continue

dogs = get_num("How many dogs do you have: ")
print(dogs)


