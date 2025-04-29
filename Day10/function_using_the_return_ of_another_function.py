def function_1(text):
    return text + text

def function_2(text):
    return text.title()

#output = function_1("hello")
output = function_2(function_1("hello"))#output of function 1 becomes the input for function 2
print(output)