# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: #change or to and
            print ("FizzBuzz")
        elif number % 3 == 0: #change if to elif
            print ("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])# remove square brackets

print(fizz_buzz(100))
