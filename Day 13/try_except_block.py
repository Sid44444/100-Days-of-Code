try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 26. ")
    age = int(input("How old are you?"))

if age >= 18:
    print (f"You can drive at age {age}.")
else:
    print ("Currently, you are too young to drive")