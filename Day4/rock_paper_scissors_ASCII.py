import random
human_choice = int(input("Welcome to the game Rock, Paper, Scissors. \nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if human_choice == 0:
    print(f"You chose {rock}")
elif human_choice == 1:
    print(f"You chose {paper}")
elif human_choice == 2:
    print(f"You chose {scissors}")
else:
    print("Invalid choice, please choose again")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(f"The computer chose {rock}")
elif computer_choice == 1:
    print(f"The computer chose {paper}")
elif computer_choice == 2:
    print(f"The computer chose {scissors}")

if human_choice == 0 and computer_choice == 1:
    print("The computer wins")
elif human_choice == 0 and computer_choice == 2:
    print("The human wins")
elif human_choice == 1 and computer_choice == 0:
    print("The human wins")
elif human_choice == 1 and computer_choice == 2:
    print("The computer wins")
elif human_choice == 2 and computer_choice == 0:
    print("The computer wins")
elif human_choice == 2 and computer_choice == 1:
    print("The human wins")
if human_choice == computer_choice:
    print("Draw")
