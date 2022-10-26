#Good or Bad Day?


with open('Good_day.txt', 'r') as good:
    last_line = good.readlines()[-1]

def set_current():
    while True:
        if last_line == "I am glad you had a good day!":
            print("Hello User!\nLast time you said you were having a good day. Keep it up!")
            break
        elif last_line == "I sorry I had your haveing a bad day!": 
            print("Hello User!\nLast time  you said you were haveing a bad day. I hope things get better!")
            break
        else:
            print("Whoops")
            exit()

def day_check():
    while True:
        try:
            GoodOrBad = input("Are you haveing a good day [Y|n]: ").lower()
        except ValueError:
            print("Please enter ""Y""for good day and, ""N"" for bad day.")
        else:
            if GoodOrBad == "y" or GoodOrBad == "" or GoodOrBad =="n":
                if GoodOrBad == "y" or GoodOrBad == "":
                    grades_file = open('Good_day.txt', 'a')
                    grades_file.write("\nI am glad you had a good day!")
                    grades_file.close()
                    print("I am glad you had a good day!")
                    return GoodOrBad
                    break
                else:
                    grades_file = open('Good_day.txt', 'a')
                    grades_file.write("\nI sorry I had your haveing a bad day!")
                    grades_file.close()
                    print("I sorry I had your haveing a bad day!")
                    return GoodOrBad
                    break
            else:
                print("Please enter ""Y"" for good day and, ""N"" for bad day.")

def main():
    set_current()
    day_check()

main()