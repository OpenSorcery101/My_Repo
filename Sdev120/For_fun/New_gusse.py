from random import randint

def get_num():
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


def play_again():
    while True:
        again=input("Would you like to play again [Y|n]" )
        if again in ['y','']:
            main()
        elif again == 'n':
            exit()
        else:
            print("Plese  select 'y' for yes and 'n' for no")

def main():
    number = randint(1,100)
    count = 0
    while count < 5 :
        guess = get_num()
        if number > guess: 
            print("Your gusse is to low")
            count +=1
        elif number < guess: 
            print("Your gusse is to high")
            count += 1
        else:
            print("You gussed the number")
            break
    if count == 5:
        print("You lose, the number was " + str(number))

main()
