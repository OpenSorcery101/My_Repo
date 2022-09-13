def get_price():
    while True:
        try:
            x= float(input("Enter the price of the meal: "))
            if x < 0: 
                print("Please don't use negatice numbers.")
                continue
            else:
                break
        except ValueError:
            print("Please use a number")
            continue
    return x

def main():
    name_list = []
    price_list = []
    go_again = "y"

    while go_again  != 'n':
        name_list.append(input("Who ate a meal: "))
        price_list.append(get_price())
        while True:
            go_again = input("Do you have more people to add? [Y|n]: ").lower()
            if go_again in ['y','','n']:
                break
            else:
                print("Please use a 'y' for yes or 'n' for no")
    total = sum(price_list)
    item_in_list = len(price_list)
    avarage = total / item_in_list
    for person, price in zip(name_list, price_list):
        diff = avarage - price
        print(person, "paid" , price, "which is", diff,"from the average." )
        if diff < 0:
            diff = abs(diff)
            print(person, "paid $", diff, "above the average.")
        elif diff == 0:
            print(person, "paid $", diff, " which is the average.")
        else:
            print(person, "paid $", diff, "below the average.")
    
main()