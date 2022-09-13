import random 


number = random.randint(1,100)
print(number)


counter = 6
while counter > 1:
    counter = counter - 1 
    user_number = int(input("Please enter a whole number!: "))
    print("You have " + str(counter) + " guesses left!")
    if user_number < 1:
        print("Please enter a whole number equal to or greater to 1")
        continue
        break
    elif user_number > 100:
        print("please enter a whole number equal to or less than 100")
        continue
        break
    elif counter == 1:
        print("You ran out of attempts!")
        print("The magic number is " + str(number))
        break
    elif user_number == number:
        print("You Win! \nThe magic number was " + str(number))
        break
    elif user_number < number:
        print("Your number is  to high!")
        continue
        break
    elif user_number > number:
        print("You number was to low!")
        continue
        break

