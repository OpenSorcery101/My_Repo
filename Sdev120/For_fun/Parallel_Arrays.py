name_lsit= []
price_list =  []

#name_lsit.append(input("Please enter your name: "))
#price_list.append(input("Pleease enter you cost: "))

#final_list= zip(name_lsit,price_list)
#print(final_list)

'''
name_lsit.append(input("Please enter your name: "))
price_list.append(input("Pleease enter you cost: "))
question = input("Do you have another perons?: y|N ")

if question == "y" or  question == "Y":
    print("go")
else:
    final_list = zip(name_lsit, price_list)
    print(list(final_list))
'''

def add_list(self):
    name_lsit.append(input("Please enter your name: "))
    price_list.append(input("Pleease enter you cost: "))
    Choice = input("Do you have another perons?: y|N ")
    if Choice == "y" or Choice == "Y":
        add_list(self)
    else:
        Choice == "N"
        final_list = zip(name_lsit, price_list)
        print(list(final_list))



add_list()

print() 