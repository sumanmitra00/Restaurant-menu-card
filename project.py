#Menu

menu = {
    'Veg-Rice' : 30,
    'Egg-Rice' : 35,
    'Fish-Rice' : 45,
    'Meat-Rice' : 50,
    'Cold drinks' : 20,
}

print("Welcome to our Restaurant")
print("The menu is given below. Please select your menu.\nVeg-Rice : 30\nEgg-Rice : 35\nFish-Rice : 45\nMeat-Rice : 50\nCold drinks : 20")

order_value = 0

item1 = input("Enter your order : ")
if item1 in menu:
    order_value += menu[item1]
    print(f"Your item {item1} has been added to menu")
    
else:
    print(f"Item{item1} not available in menu")
    
another_other = input("Are you want to order anything? (Yes/No) : ")
if another_other == "Yes":
    item2 = input("Enter your second order : ")
    if item2 in menu:
        order_value += menu[item2]
        print(f"{item2} has been added to your menu")
        
    else:
        print(f"Ordered item{item2} is not available currently")

print(f"The total amount of items : {order_value}")
        
    