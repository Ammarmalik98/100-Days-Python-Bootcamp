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

import random
print("Rock, Paper, Scissors, Scissors\nPress 0. for Rock, 1. for Paper, 2. for Scissors, 3. for Scissors")

user_input = int(input("Enter your choice: "))
computer_input = random.randint(0, 2)

if user_input == 0 and computer_input == 0:
    print(f"{rock} vs {rock}")
    print("It's a Draw")
elif user_input == 1 and computer_input == 1:
    print(f"{paper} vs {paper}")
    print("It's a Draw")
elif user_input == 2 and computer_input == 2:
    print(f"{scissors} vs {scissors}")
    print("It's a Draw")
elif user_input == 0 and computer_input == 1:
    print(f"{rock} vs {paper}")
    print("Sorry, you lost")
elif user_input == 0 and computer_input == 2:
    print(f"{rock} vs {scissors}")
    print("Congrats, you won")
elif user_input == 1 and computer_input == 0:
    print(f"{paper} vs {rock}")
    print("Congrats, you won")
elif user_input == 1 and computer_input == 2:
    print(f"{paper} vs {scissors}")
    print("Sorry, you lost")
elif user_input == 2 and computer_input == 0:
    print(f"{scissors} vs {rock}")
    print("Sorry, you lost")
elif user_input == 2 and computer_input == 1:
    print(f"{scissors} vs {paper}")
    print("Congrats, you won")
else:
    print("Your dumbass choose a wrong number")
