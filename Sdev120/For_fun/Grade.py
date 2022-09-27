#Grade Calculator
import statistics

#Create List
name_list = []
grade_list = []
Letter_list = []

# Input Student Name
def get_student():
    while True:
        try:
            Student_name = input("What is you name?: ")
            name_list.append(Student_name)
            return Student_name
        except ValueError:
            print("Please Enter Students Name")

#Input Student Grade
def get_grade():
    while True:
        try:
            Student_grade = input("Please enter Student grade:  ").upper()
        except ValueError:
            print("Please enter a Letter Grade [A, B, C, D, F]")
        else:
            if Student_grade =='A' or Student_grade =='B' or Student_grade =='C'or Student_grade =='D' or Student_grade =='F':
                grade_list.append(Student_grade)
                #Convert A, B, C, D, F -> 4, 3, 2, 1
                if Student_grade == 'A':
                    Letter_list.append(4)
                    return Student_grade
                    break
                elif Student_grade == 'B':
                    Letter_list.append(3)
                    return Student_grade
                    break
                elif Student_grade == 'C':
                    Letter_list.append(2)
                    return Student_grade
                    break
                elif Student_grade == 'D':
                    Letter_list.append(1)
                    return Student_grade
                    break
                else:
                    Letter_list.append(0)
                    return Student_grade
                    break
            else:
                print("Please enter a Letter Grade [A, B, C, D, F] ")


#Main Function
def main():
    while True:
        get_student()
        get_grade()
        #Ask to go again
        try:
            again = input("Do you want to add another entry?: [Y|n] ").lower()
            if again == "y":
                continue
            else:
                break
        except ValueError:
            print("Please pick Y for yes and N for no. ")


main()
#Convert Letter list to find the mean
mean = statistics.mean(Letter_list)

#Merge Name list and Grade list
final_list=list(zip(name_list,grade_list))
final_list = str(final_list)
#Display to screen findings
print(f"The Class list is {final_list} and the class average is {mean}")

##### Extra Output to text file
grades_file = open('Grade.txt', 'w')
grades_file.write(f"The Class list is {final_list} \n and the class average is {mean}")
grades_file.close()

 
