year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print ("You are a Gen Z.")

#The bug is that 1994 is not catered for.
#The first part of the if statement is printed if the year is less than 1994
#The elif statement is for greater than 1994.
#Currently, nothing will print if the input year is 1994.

#To fix the bug and = sign needs to be added after either the < sign on line 3 or the > sign on line 5.
