programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

#by using the key the value can be printed, data type remains important.
print(programming_dictionary["Bug"])


#Adding a new entry [Key]=value
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#An empty dictionary can be created by->
empty_dictionary = {}
#AN empty list->
empty_list = []

#Wipe and empty_dictionary
#programming_dictionary = {}
#print (programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary printing key only
for key in programming_dictionary:
    print(key)

#Loop through a dictionary printing key followed by its value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

