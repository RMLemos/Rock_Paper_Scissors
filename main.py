import random

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

game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors.\nWhat do you choose?")
player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[player_choice])

print("Computer chose:")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

# rocks wins against scissors.
# scissors wins against paper.
# paper wins against rock.

if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == computer_choice:
    print("It's a draw")
else:
    print("You lose!")
