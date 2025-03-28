#Write code using the modulo operator and conditional checks in Python to check if the number in the input area is odd or even.
#If odd print "Odd" otherwise printout "Even"

number_to_check=int(input("Please provide a whole number and we will let you know if it is odd or even: "))
if number_to_check % 2 != 0:
    print ("Odd")
else:
    print("Even")