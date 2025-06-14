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

resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 300,
}

money = 0

def is_resources_sufficient(order_ingredients):
    """Returns True if the order can be made, False if the ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! there is not enough {item} in the machine.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?:  ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """ Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print (f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money, have a refund.")
        return False

def make_drink(drink_name, order_ingredients):
    """Subtract the ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

machine_on = True

while machine_on:
    """Functionality of machine when on "off", "report", "drink"""
    user_input = input ("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        print ("Goodbye")
        machine_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[user_input]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(user_input, drink["ingredients"])







