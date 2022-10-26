from re import M


menu_items = {"Burger":5.99,"Cheese Burger":6.49,"Fries":2.49,"Drink":1.99}
menu_items["Hot Dog"] =2.99
print(menu_items)
menu_items.update({"Burger":6.59,"Cheese Burger":6.49,"Fries":2.49,"Drink":1.99, "Hot Dog":3.49})

#print(menu_items.items())
#for key, value in menu_items.items():
#    print(key, value)

def get_key(arg, dictionary):
    my_list = []
    for key, value in dictionary.items():
        if value ==arg:
            my_list.append(key)
    return key

print(get_key(1.99, menu_items))


my_order = ['Cheese Burger',"Cheese Burger", "Fries", "Drink","Hot Dog","Fries", "Drink","Burger","Drink"]
count = {}
total = 0
for i in my_order:
    count[i]=count.get(i, 0) + 1
print(count)
for item, amount in count.items():
    price = menu_items[item]
    total = total + (price * amount)
print(total)