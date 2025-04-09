import random
from hangman_art import logo
from hangman_words import word_list

print(logo)

#word_list = ["aardvark", "baboon", "camel"]
#TODO-1: -Update the word list to use the word_list from hangman_words.py


#Create a variable called 'lives' to keep track of the number of lives left. Set lives to equal 6.
lives = 6
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
chosen_word = random.choice(word_list)  # randomly chooses a word from the word_list and assigns it to a variable called chosen_word
print(chosen_word)

# Create an empty string called "placeholder".
# for each letter in chosen_word, add a _ to placeholder
# same number of blanks as the word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Use a while loop to let the user guess again

game_over = False
correct_letters = []  # correct guesses placed in list that is used to print the guesses to date

while not game_over:
    guess = input("Guess a letter: ").lower()  # ask user to guess a letter and assign their answer to a variable called guess. Make lowercase.
    #print (guess)

    # Create a display that put the guess letter in the right place.

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    #If guess is not a letter in the chosen_word. Then reduce lives by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print ("You lose.")


    if "_" not in display: #no more letters to guess
        game_over = True
        print("You win")

# print the ASCII art from 'stages'
# that corresponds to the current number of lives the user has remaining.
    from hangman_art import stages

    print(stages[lives])