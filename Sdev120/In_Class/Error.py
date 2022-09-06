#x = int(input("Give me that number"))
#print(x)

#Check for number
##Will aks use to try again untill they put in an integer
'''
while True:
    try:
        x = int(input("Give me that number: "))
        break
    except:
        print("You did not give me that number")
        continue
print(x)
'''
#Checking for Value  Errors
while True:
    try:
        x = int(input("Give me that number: "))
        break
    except ValueError:
        print("You did not give me that number")
        continue
print(x)
