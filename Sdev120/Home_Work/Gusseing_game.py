import random 
import os   

number = random.randint(1,100)

question = "y"
counter = 0 
while counter < 5 or question =="y": 
    number = number
    counter = counter + 1
    user_num = int(input("Please enter a whole number between 1 - 100: "))
    if counter == 5:
            os.system('cls')
            print("You ran out of gusses the magic number was " + str(number))
            question = input("Would you like to play again? y|N ").lower
            number = random.randint(1,100)
    else:
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
         print("No")