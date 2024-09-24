# Display art
from art import logo,vs
print(logo)

# generate a random account
import random
from game_data import data

def format_choices(choice):
    choice_name = choice['name']
    choice_description = choice['description']
    choice_country = choice['country']
    return f"{choice['name']} from {choice['country']} is a {choice['description']}"

def check_followers(guess,followers_a,followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'

choice_b = random.choice(data)
points = 0
game_on = True

while game_on:
    choice_a = choice_b
    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)

    # format account into printable format
    print(f"Choice A : {format_choices(choice_a)}.")
    print(vs)
    print(f"Choice B : {format_choices(choice_b)}.")
    # ask user for a guess
    selection = input("who has more followers. Type 'A' or 'B'. ").lower()
    choice_a_followers = choice_a['follower_count']
    choice_b_followers = choice_b['follower_count']

    correct_guess = check_followers(selection, choice_a_followers, choice_b_followers)

    if correct_guess:
        points += 1
        print()
        print("you win")
        print(f"score is {points}")
    else:
        print("you lose")
        print(f"score is {points}")
        game_on = False
# chec



