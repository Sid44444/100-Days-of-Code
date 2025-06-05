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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#TODO: 1 Prompt user by asking which drink they would like while loop activated
#TODO: 2 Break while loop in input is 'off' to switch the machine off
#TODO: 3 Once drink is dispensed the while loop should star again
#TODO: 4 Report should be printed to screen when 'report' typed in to input listing current resource values
#TODO: 5 Check resources sufficient to make drink order
#TODO: 6 If insufficient resources print "Sorry there is not enough {ingredient}."
#TODO: 7 If sufficient ingredients, program to prompt user to insert coins
#TODO: 8 Quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#TODO: 9 Calculate the monetary value of the coins inserted eg, 3 quarters, 2 dimes, 1 nickel
#TODO: 10 Check transaction, has the user inserted enough money?
#TODO: 11 If not enough money "Sorry that's not enough money. Money refunded."
#TODO: 12 If user has inserted enough money cost of drink added to profit of machine (for the report)
#TODO: 13 if user has inserted too much money the machine should offer change.
#TODO: 14 "Here is $2.45 dollars in change." Round to 2 decimal places
#TODO: 15 Make a coffee. If transaction is successful and enough resources the ingredients should be deducted from the coffee machine resources
#TODO: 16 Once resources have been deducted tell the user "Here is your latte. Enjoy!"
#

