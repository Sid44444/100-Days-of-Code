import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#TODO- ASCII art

guesses = int(0)
attempt_to_guess = 0

#function to check user_guess against actual number
def guess_feedback(user_guess, actual_num, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_num:
        print ("Too high")
        return turns -1
    elif user_guess < actual_num:
        print ("Too low")
        return turns -1
    elif user_guess == actual_num:
        print (f"You got it! The number was {actual_num}!")
        #start_new_game()
    else:
        print ("Please enter a valid number")


#function to set difficulty
def level_selected():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def start_new_game():
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100")
    actual_num = random.randint(1, 100)
    print(f"Pssst, the correct answer is {actual_num}")

    turns = level_selected()


    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != actual_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess:"))
        turns = guess_feedback(guess, actual_num, turns)
        if turns  == 0:
            print("You run out of guesses, you lose")
            return
        
start_new_game()


def end_game(user_guess, actual_num):
    if user_guess == actual_num:
        question = input("type 'y' for another game or 'n' to exit: ")
        if question == 'y':
            start_new_game()
        else:
            print("Goodbye")



#level_selected()
#number_to_guess()

    #if attempt_to_guess == num:





