import os 
import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0, 
    }
}
used_water = 0
used_milk = 0
used_coffee = 0
amount_of_water = 400
amount_of_milk = 800
amount_of_coffee = 100
def report(): 
    global used_water, used_coffee, used_milk, amount_of_water, amount_of_coffee, amount_of_milk
    amount_of_water -= used_water
    amount_of_milk -= used_milk
    amount_of_coffee -= used_coffee
    return amount_of_water, amount_of_milk, amount_of_coffee
def make_latte():
    global used_water,used_milk,used_coffee
    used_water = MENU["latte"]["ingredients"]["water"]
    used_milk = MENU["latte"]["ingredients"]["milk"]
    used_coffee = MENU["latte"]["ingredients"]["coffee"]
    return used_water, used_milk, used_coffee
def make_espresso():
    global used_water,used_milk,used_coffee
    used_water = MENU["espresso"]["ingredients"]["water"]
    used_coffee = MENU["espresso"]["ingredients"]["coffee"]
    return used_water, used_milk, used_coffee
def make_cappuccino():
    global used_water,used_milk,used_coffee
    used_water = MENU["cappuccino"]["ingredients"]["water"]
    used_milk = MENU["cappuccino"]["ingredients"]["milk"]
    used_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    return used_water, used_milk, used_coffee
if_coffee_machine_is_on = True
while if_coffee_machine_is_on is True:
    total_amount = 0
    ask_the_user = int(input("What coffee do you want to drink: (Press 0 for Espresso, Press 1 for Latte, Press 2 for Cappuccino and Press 3 for Report)\n"))
    ten_notes = int(input("How many notes of ten: "))
    twenty_notes = int(input("How many notes of twenty: "))
    fifty_notes = int(input("How many notes of fifty: "))
    hundred_notes = int(input("How many notes of hundred: "))
    total_amount = ten_notes*10 + twenty_notes*20 + fifty_notes*50 + hundred_notes*100
    if ask_the_user == 0 and amount_of_water != 0 and amount_of_milk != 0 and amount_of_coffee != 0 and total_amount >= 200:
        make_espresso()
        report()
        print("Thus your espresso is made successfully")
        if total_amount >=200:
            amount = total_amount - 200
            print(f"Your change is {amount}")
    elif ask_the_user == 1 and amount_of_water != 0 and amount_of_milk != 0 and amount_of_coffee != 0 and total_amount>=500:
        make_latte()
        report()
        print("Thus your latte is made successfully")
        if total_amount >=500:
            amount = total_amount - 500
            print(f"Your change is {amount}")
    elif ask_the_user == 2 and amount_of_water != 0 and amount_of_milk != 0 and amount_of_coffee != 0 and total_amount>=700:
        make_cappuccino()
        report()
        print("Thus your cappuccino is made successfully")
        if total_amount >=700:
            amount = total_amount - 700
            print(f"Your change is {amount} ")
    elif ask_the_user == 3:
        print(f"The amount of milk left is {amount_of_milk}, the amount of water {amount_of_water} and the amount of coffee left is {amount_of_coffee}")
    elif total_amount<200:
        print("The amount you paid is not enough")
    else:
        print("The amount of water, milk and coffee is not enough to make the coffee")
        print(f"The amount of milk left is {amount_of_milk}, the amount of water {amount_of_water} and the amount of coffee left is {amount_of_coffee}")
        break
    time.sleep(5)
    os.system('cls')        

    
