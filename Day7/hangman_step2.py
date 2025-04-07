import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = (random.choice(word_list))#randomly chooses a word from the word_list and assigns it to a variable called chosen_word
print (chosen_word)

#TODO-1: Create an empty string called "placeholder".
# for each letter in chosen_word, add a _ to pplaceholder
# same number of blanks as the word.
placeholder=("")
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print (placeholder)


guess= input("\nGuess a letter: ").lower()#ask user to guess a letter and assign their answer to a variable called guess. Make lowercase.
#print (guess)

#TODO-2: Create a display that put the guess letter in the right place.

display=""
for letter in chosen_word : 
    if letter == guess:
        display += letter
    else:
        display += ("_")

print(display)