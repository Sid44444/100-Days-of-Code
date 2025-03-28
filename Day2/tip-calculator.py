#welcome message
print("Welcome to the tip calculator!")
#flost type input in $
bill_amount=float(input("What was the total bill? $"))
#int input for tip percentage
tip=int(input("What percentage tip would you like to give? 10, 12, 15 "))
#number of people sharing
people=int(input("How many people is the bill to be split between? "))
#calculate bill plus tip amount
bill_with_tip=bill_amount/100*tip + bill_amount
#divide the total bill by the number of people
each_person_payment=bill_with_tip/people
#round the person total payment to 2 decimal places
person_total_payment=round(each_person_payment,2)
#print the amount each person needs to pay
print(f"Each person should pay: ${person_total_payment}")

