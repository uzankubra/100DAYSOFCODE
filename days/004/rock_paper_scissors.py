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

#Write your code below this line 👇

game_choices = [rock, paper, scissors]

print("Welcome the game")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

print("Your choice:\n")
print(game_choices[user_choice])

# Computer choice
import random

computer_choise = random.randint(0, 2)

print("Computer choice:\n")
print(game_choices[computer_choise])

# algorithm
if user_choice >= 3 or user_choice < 0:
    print("Invalid type!")

elif computer_choise == 0 and user_choice == 1:
    print("you win.")

elif user_choice == 0 and user_choice == 1:
    print("you lose")

elif computer_choise > user_choice:
    print("you lose")

elif user_choice > computer_choise:
    print("you win")

elif computer_choise == user_choice:
    print("It's a draw")
