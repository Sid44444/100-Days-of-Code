import random
#import art
#print(art.logo)

print("Welcome to Blackjack!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

def card_selection():
    card = random.choice(cards)
    return card


def player_card():
    player_cards.append(card_selection())


def computer_card():
    computer_cards.append(card_selection())

#Your cards:
#Computer's first card:)
#Type 'y' to get another card, type 'n' to pass:
#Computer's first card:
#Your final hand: [10, 10], final score: 20
#You went over. You lose emoji
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if game_start == 'y':
    player_card()
    computer_card()
else:
    print ("Goodbye")

print(f"Your first card is {player_cards}")
print(f"The computer's first card is {computer_cards}")

another_card = input("Type 'y' to get another card, type 'n' to pass:")
if another_card == "y":
    player_card()
    computer_card()
print(f"Your cards are: {player_cards}")

third_card = input("Type 'y' to get another card, type 'n' to pass:")
if third_card == "y":
    player_card()
elif third_card == "n":
    print(f"Your final hand: {player_cards}, final score {sum(player_cards)}")
else:
    print("invalid input, please type 'y' or 'no'")
if sum(computer_cards) >= 17:
    print(f"The computers final hand: {player_cards}, final score {sum(player_cards)}")

if sum(computer_cards) >21:
    print("the computer looses")


#print(f"Your cards are: {player_cards}")