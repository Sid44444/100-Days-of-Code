#This is a love calculator
print("Welcome to the true love calculator!")
name1 = input("Please enter the first name: ")
name2 = input("Please enter the second name: ")


def calculate_love_score(name1, name2):#no need to keep name separate so combine
    combined_names = name1 + name2
    lower_names =combined_names.lower()
    #print (lower_names)
    #for letter in combined_names.lower():
    first_digit, second_digit = 0, 0
    #for loop used below but if score above 9 the score is printed
    # as such eg truetrue and lovelove prints out 1010
    for digit in [lower_names]:

        for letter in ["t", "r", "u", "e"]:
            first_digit += lower_names.count(letter)

        for letter in ["l", "o", "v", "e"]:
            second_digit += lower_names.count(letter)

    score = int(str(first_digit) + str(second_digit))
    return score


print("The love score for the names given are: ")
print (calculate_love_score(name1, name2))
