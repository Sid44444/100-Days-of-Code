import random
from art import logo

def card_selection():
    # function to select a random card from the list 'cards'
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score_cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #this 0 represents blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It is a draw ."
    elif c_score == 0:
        return "You lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    players = 2
    is_game_over = False


    for i in range(players):
        player_cards.append(card_selection())
        computer_cards.append(card_selection())

    while not is_game_over:
        user_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards so far are {player_cards}, current_score: {user_score}")
        print(f"The computers first card is:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you wish to have another card? Type 'y' for yes and 'n' for no.")
            if user_should_deal == "y":
                player_cards.append(card_selection())
                print(player_cards)
            else:
                is_game_over = True


    while computer_score != 0 and computer_score <17:
        computer_cards.append(card_selection())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand:{player_cards},final score: {sum(player_cards)}")
    print(f"Computers final hand:{computer_cards},final score: {sum(computer_cards)}")
    print(compare(user_score, computer_score))





    if sum(player_cards)  < 17:
        print("The score is too low, have another card.")
        player_cards.append(card_selection())
        print(player_cards)

    if sum(computer_cards) < 17:
        print("The computers score is too low, have another card.")
        player_cards.append(card_selection())
        print(computer_cards)


    if sum(computer_cards) >= 21:
        print("The computers score is higher than 21, so the computer looses")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
