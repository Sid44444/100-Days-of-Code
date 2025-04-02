import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "8", "0"]
symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-"]
characters = []
password = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
#easy level

for i in range (0,  nr_letters):
    characters.append(random.choice(letters))

for i in range(0, nr_symbols):
    characters.append(random.choice(symbols))

for i in range(0, nr_numbers):
    characters.append(random.choice(numbers))

#mix up the order of characters using random.shuffle (list)
random.shuffle(characters)

#change the list to a string
password=' '.join(characters)

#print the shuffled new password
print(f"Your password is:{password}")