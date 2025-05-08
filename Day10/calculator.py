"""A simple calculator app"""



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

f_num = float(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
s_num = float(input("What is the next number?: "))
#prints calculation and answer using operation_symbol to access the dictionary of functions with parameters
print(f"{f_num} {operation_symbol} {s_num} = {operations[operation_symbol](f_num, s_num)}")