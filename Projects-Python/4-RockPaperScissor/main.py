# RULES
# 0 - ROCK wins against SCISSOR
# 1 - SCISSOR wins against PAPER
# 2 - PAPER wins against ROCK

import random

game_choice = ['ROCK', 'SCISSOR', 'PAPER']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissor and 2 for Paper "))
print(game_choice[user_choice])
computer_choice = random.randint(0,2)
print(game_choice[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You Typed invalid number: YOU LOSE!")
elif user_choice == computer_choice:
    print("Its a DRAW")
elif user_choice == 0 and computer_choice == 1:
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("You Win")
elif user_choice == 2 and computer_choice == 0:
    print("You Win")
else:
    print("Computer Win The game")