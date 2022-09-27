import random 
import os   

def user_number():
    while True:
        try:
            x = int(input("Give a number between 1 and 100: "))
            if x < 1 or x > 100:
                print("your number is outside the range.")
                continue
            else:
                break
        except ValueError:
            print("You did not enter a whole numbe. Please try again.")
            continue
    return x

def get_question():
    while True:
        try:
            x = input("Would you like to ply again? [y|N]: ").lower()
            if x not ['y','n']:
                print("Please enter a 'y' or 'n' ")
                continue
            else:
                break 
        except ValueError:
            print("Press 'y' for yes or 'n' for no")
            continue
    return x

## test for only  str


number = random.randint(1,100)

question = "y"
counter = 0 
while counter < 5 or question =="y" or question =="Y": 
    number = number
    counter = counter + 1
    user_num = user_number()
    if counter == 5:
            os.system('cls')
            print("You ran out of gusses the magic number was " + str(number))
            question = get_question()
            if question == 'y':
                counter = 0
                number =random.randint(1,100)
            else:
                os.system('cls')
                print("Thanks for playing!")
                exit()
    if user_num >= 1 and user_num <= 100:
        if user_num > number and counter <= 5:
            os.system('cls')
            print("your number is to high! Try Again!\n" + "You have used " + str(counter) +" /5 Gusses" )
        elif user_num < number and counter <=5:
            os.system('cls')
            print("You number is to low! Try Again!\n"+ "You have used " + str(counter) +" /5 Gusses")
        elif user_num  == number and counter <=5:
            os.system('cls')
            print("You found the magic number!")
        else:
            print("second no")
    else:
        print("No one")
if counter == 5 and question == "y":
    number = random.randint(1,100)
else:
    exit()
    