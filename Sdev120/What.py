uncle_sam = 1.08
pay_the_server = 1.15
food_stuff = input("How much was your meal? ")
corprate_cut = (float(uncle_sam)) * (float(food_stuff))
pocketbookpain = (float(corprate_cut)) * (float(pay_the_server))
pocket_book_pain= round(pocketbookpain,2)
print("You need to leave " + (str(pocket_book_pain)) + " on the table to cover tax and tip.")
