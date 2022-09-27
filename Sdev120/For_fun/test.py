#Quiz
'''
score = 0

q1 = ["When was Fortnite Battle Royale relase","When was Doublle pump patched","How many 90's can Jacob crank in 60 sec","What did Tyler Blevins say to the 8 year old child live on stream?","How good is fortnite","Best Fortnite skin","Best Fortnite camio","Best Fortnitie dance","Where did the burger land","Who got banned from Fortnite","Fortnite:"]
a1 = ["July 21, 2017","Febuary 2018","All of them","The **** did you say to me you little ****","Bad","Big Chugs","Default","California desert","Jarvis","yes"]

score_list=list(zip(q1,a1))
print(score_list)
'''

# When was Fortnite Battle Royale relase (July 21, 2017)
# When was Doublle pump patched (Febuary 2018)
# How many 90's can Jacob crank in 60 sec (All of them)
# What did Tyler Blevins say to the 8 year old child live on stream? (The **** did you say to me you little ****)
# How good is fortnite (Bad)
# Best Fortnite skin (Big Chugs)
# Best Fortnite camio (Chun Lee)
# Best Fortnitie dance (Default)
# Where did the burger land (California desert)
# Who got banned from Fortnite (Jarvis)
# Fortnite: (yes)

import random

q1 = ["When was Fortnite Battle Royale relase","When was Doublle pump patched","How many 90's can Jacob crank in 60 sec","What did Tyler Blevins say to the 8 year old child live on stream?","How good is fortnite","Best Fortnite skin","Best Fortnite camio","Best Fortnitie dance","Where did the burger land","Who got banned from Fortnite","Fortnite:"]
a1 = ["July 21, 2017","Febuary 2018","All of them","The **** did you say to me you little ****","Bad","Big Chugs","Default","California desert","Jarvis","yes"]

score_list=list(zip(q1,a1))
number =range(1,10)
number = list(set(number))


score = 0
def question():
    global score
    while True:
        try:
            print("When was Fortnite Battle Royale relase")
            awnser = input("A \nB \nC \nD ").lower()
            if awnser == "d":
                score = score + 1
            else:
                score = score + 0 
            return score
        except ValueError:
            print("Wrong go again")

def question_random():
    random
    

question()
print(score)
print(random.choices(number, k=10))

