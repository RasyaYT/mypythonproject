rock2 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper2 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors2 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

import random

gameImage = [rock2, paper2, scissors2]

userChoice = int(input("Enter You Choice !,Type 0 for rock, 1 for paper, and 2 for scissors:\n"))
print(gameImage[userChoice])

computerChoice = random.randint(0, 2)
print("Computer Chose: ")
print(gameImage[computerChoice])

if userChoice >= 3 or computerChoice < 0:
    print("Invalid Numer, you lose")
elif userChoice == 0 and computerChoice == 2:
    print("You Win!")
elif computerChoice == 2 and userChoice ==  0:
    print("You Lose!")
elif computerChoice > userChoice:
    print("You Lose!")
elif userChoice > computerChoice:
    print("You Win!")
elif userChoice == computerChoice:
    print("Draw")












