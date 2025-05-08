"""A simple calculator app"""
import art
from socket import EAGAIN


#operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#operation dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#def calculation(f_num, operation, s_num):

#print (operations["*"](4, 8))

def calculator():
    print(art.logo)
    should_accumulate = True
    f_num = float(input("What is the first number?: "))

    while should_accumulate:


        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        s_num = float(input("What is the next number?: "))
#prints calculation and answer using operation_symbol to access the dictionary of functions with parameters
        answer = operations[operation_symbol](f_num, s_num)
        print(f"{f_num} {operation_symbol} {s_num} = {answer}")
        use_result = input(f"Do you want to continue working with the previous result {answer}? ('y' for yes or 'n' for a new calculation: ")
        if use_result == "y":
            f_num = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()#calling a function within a function to begin again (recursion). Another while loop would have worked too.


calculator()#call function to start the program

