import random
from socket import EAGAIN

from art import logo
from art import vs
from game_data import data

score = int(0)
def game(score):
    print(logo)
    num= random.randint (0, 49)
    num2= random.randint (0, 49)
    print (num +1)
    A_name= (data[num]["name"])
    A_occupation = (data[num]["description"])
    A_country = (data[num]["country"])
    A_follower_count = (data[num]["follower_count"])
    B_name= (data[num2]["name"])
    B_occupation = (data[num2]["description"])
    B_country = (data[num2]["country"])
    B_follower_count = (data[num2]["follower_count"])
    print(f"Compare A: {A_name}, a {A_occupation}, from {A_country}.")
    print(vs)
    print(f"Against B: {B_name}, a {B_occupation}, from {B_country}.")
    answer=input("Who has more followers? Type 'A' or 'B': ").upper()
    if A_follower_count > B_follower_count and answer == 'A':
        score += 1
        print (f"You're right! Current score: {score}")
        game(score)

    elif A_follower_count < B_follower_count and answer == 'B':
        score  += 1
        print (f"You're right! Current score: {score}")
        game(score)
    else:
        print (f"Sorry, that's wrong. Final score: {score}")
        play_again =input ("Would you like to play again? Type 'Y' or 'N'" ).upper
        if play_again == 'Y':
            game(score)


game(score)
#TODO The previous A now becomes B and a new comparison happens
#TODO Get play again to work

