"""A simple calculator app"""
#input(int("What is the first number?: " ))
#print("+\n-\n*\n/\n")
#print ("Pick an operation: ")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print (operations["*"](4, 8))