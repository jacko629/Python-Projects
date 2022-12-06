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

# Write your code below this line 👇

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = 0
if player_choice == 0:
    user = rock
elif player_choice == 1:
    user = paper
elif player_choice == 2:
    user = scissors
else:
    print("Try again. Make sure you type in only a 0 ,1 or 2.")

print(f"\nYou chose:\n{user}")

print("\nComputer chose:")

rps = [rock, paper, scissors]
index = len(rps) - 1
# computer logic
computer = 0
rockpapers = random.randint(0, index)
if rockpapers == 0:
    computer = rock
elif rockpapers == 1:
    computer = paper

elif rockpapers == 2:
    computer = scissors

print(computer)

# winner
if user == rock and computer == scissors:
    print("\nYou win")
elif user == scissors and computer == paper:
    print("\nYou win!")
elif user == paper and computer == rock:
    print("\nYou win!")
elif user == computer:
    print("\nIts a tie")
else:
    print("\nYou lose!")



