#Data Types

#String
#Taking out an element from a string is called subscripting
print("Hello"[4])
#minus number may also be used
print("Hello"[-4])

#integer = whole number (positive and negative)

#this print statement will print 468
print(123 + 345)

#underscores can be used to see numbers clearly as the computer ignores them
#this is useful for large numbers/integers
123_456_789

#Float, short for floating point number
3.14159

#Boolean
True
False

#len function below will give an error function as it does not like working with integers
#len(12345)
#In order to make this function work we need to change the data type to a string.
print(len("hello"))

#type checking
print(type("Hello"))#prints "class 'str'"
print(type(12345))#prints "class 'int'"
print(type(123.45))#prints "class 'float'"
print(type(True))#prints "class 'bool'"

#Type conversion or Type casting
print(int("123") + int("456"))


#change this code so that no error occur: print("Number of letters in your name: " + str(len(input("Enter your name"))))
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
#or
name_of_user = input("Enter your name: ")
length_of_name = len(name_of_user)

print("Number of letters in your name: " + str(length_of_name))