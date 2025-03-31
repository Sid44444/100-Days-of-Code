#logical operators 'and' 'or' 'not'

#update code so that people age 45 to 55 (inclusive) ride for free. Use logical operators to check that the age is greater than 45, and it is also less than 55.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age >= 45 and age <= 55: #this statement can be simplified but for a beginner this code is easier to understand
        bill = 0
        print("You have been selected to ride for free")
    elif age >= 18:
        bill = 12
        print("Adult tickets are $12.")
    elif age >=12:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.")



    wants_photo= input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        #Add $3 to bill
        bill += 3 #same as bill = bill + 3
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")