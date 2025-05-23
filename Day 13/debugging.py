def my_function():
    for i in range (1, 20):
        if i == 20:
            print ("You got it")

my_function()

# The problem here if the range chosen never reaches 20. range goes from 1-19 not including 20
# To fix this bug change range from (1, 20) to (1, 21)