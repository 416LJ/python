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
your_number_choice = int(input("please select a number 1, 2, or 3\n1 is rock\n2 is paper\n3 is scissors\n"))
your_choice = ""


if your_number_choice == 1:
    your_choice = rock
    print(f"you chose\n{your_choice}")
if your_number_choice == 2:
    your_choice = paper
    print(f"you chose\n{your_choice}")
if your_number_choice == 3:
    your_choice = scissors
    print(f"you chose\n{your_choice}")

random_choice = random.randint(1,3)

if random_choice == 1:
    random_choice = rock
    print(f"computer chose\n{random_choice}")
if random_choice == 2:
    random_choice = paper
    print(f"computer chose\n{random_choice}")
if random_choice == 3:
    random_choice = scissors
    print(f"computer chose\n{random_choice}")

