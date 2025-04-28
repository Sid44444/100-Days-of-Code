import art_gavel


print(art_gavel.logo)

print("Welcome to the secret auction program.")

def highest_bidder(bidders_dictionary):
    winner = ""
    highest_bid = 0

    max(bidders_dictionary)

    for bidder in bidders_dictionary:
        bid_amount = bidders_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of £{highest_bid}")

bidders_and_bid = {}#outside while loop so data accumulates. Dictionary created.

continue_with_another=True
while continue_with_another:
    name_input = input("What is your name?")
    bid_value = int(input("What is your bid? £"))#data type changed to an integer
    bidders_and_bid[name_input] = bid_value
    another_bidder = (input("Is there another bidder? Type 'y' for yes or 'n' for no. \n")).lower()
    print(bidders_and_bid)
    if another_bidder == 'n':
        continue_with_another = False
        highest_bidder(bidders_and_bid)
    elif continue_with_another == "y":
        print("\n" *20)  # clear screen so bidders do not see others bids.

