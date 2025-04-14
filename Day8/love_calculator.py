#This is a love calculator
print("Welcome to the true love calculator!")
name1 = input("Please enter the first name: ")
name2 = input("Please enter the second name: ")


def calculate_love_score(name1, name2):#no need to keep name separate so combine
    combined_names = name1 + name2
    lower_names =combined_names.lower()
    #print (lower_names)

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e #may be a better way of doing this as the code repeats

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    return score


print("The love score for the names given are: ")
print (calculate_love_score(name1, name2))
