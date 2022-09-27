#Calculator
import os


def get_float():
    os.system("cls" if os.name == 'nt' else "clear")
    while True:
        try:
            x = float(input("Please enter a number: "))
            return x
        except ValueError:
            print("Enter an integer or a float number.")
            continue

def operation():
    while True:
        try:
            x = input("What opertaion whould you like to use? [+, -, /, *, =]: ")
            if x == "+":
                return x
            elif x == "-":
                return x
            elif x == "/":
                return x
            elif x == "*":
                return x
            elif x == "=":
                return x
            else:
                print("\nPlease select + for addition, - for subratction, / for division, * for multiplication, = for equall\n")
                continue
        except ValueError:
            print("Please select + for addition, - for subratction, / for division, * for multiplication")

def calculation():
    print("yes")

def main():
    num_list = []
    op_list = []
    while True:
        num = get_float()
        op = operation()
        num_list.append(num)
        op_list.append(op)
        try:
            question = input("Would you like to add more? [n|Y]: ").lower()
            if question == "y":
                continue
            else:
                print(list(zip(num_list, op_list)))
                break
        except ValueError:
            print("Whoops")
            exit()


                
main()
