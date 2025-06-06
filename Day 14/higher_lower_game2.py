from art import logo, vs

from game_data import data

import random

#Format the account data into printable format.
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"

print (logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    #Generate a randon account data from the game data

    #Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b: #make sure that account a and b are different.
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #account_name = account_a

    #ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

#Clear the screen
    print("\n" * 20)
    print(logo)

    #Check if user got it right
    #get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct =  check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_should_continue = False
#Use if statement to check if user is correct