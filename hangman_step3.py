import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = (random.choice(word_list))#randomly chooses a word from the word_list and assigns it to a variable called chosen_word
print (chosen_word)

# Create an empty string called "placeholder".
# for each letter in chosen_word, add a _ to placeholder
# same number of blanks as the word.
placeholder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print (placeholder)

#Use a while loop to let the user guess again

game_over = False
correct_letters = [] #correct guesses placed in list that is used to print the guesses to date

while not game_over:
    guess= input("Guess a letter: ").lower()#ask user to guess a letter and assign their answer to a variable called guess. Make lowercase.
#print (guess)

#Create a display that put the guess letter in the right place.

    display= ""

    for letter in chosen_word :
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if "_" not in display:
        game_over = True
        print("You win")

