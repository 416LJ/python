from random import random, randint

from game_data import data
from art import logo,vs

def select_people():
    rand_p1 = randint(0, len(data)-1)
    rand_p2 = randint(0, len(data)-1)
    while rand_p1 == rand_p2:
        rand_p1 = randint(0, len(data)-1)
        rand_p2 = randint(0, len(data)-1)

    return rand_p1,rand_p2

game_lose = False
points = 0
while not game_lose:
    print("\n" * 20)
    print(logo)
    people = select_people()
    p1 = people[0]
    p2 = people[1]
    p1_followers = data[p1]['follower_count']
    p2_followers = data[p2]['follower_count']
    print(f"your current score is : {points}")
    print(f"Compare A: {data[p1]['name']}, a {data[p1]['description']}, from {data[p1]['country']}")
    print(vs)
    print(f"Compare A: {data[p2]['name']}, a {data[p2]['description']}, from {data[p2]['country']}")
    selection = input("who has more followers. Type 'A' or 'B'. ")
    if selection == 'A':
        selection = data[p1]['follower_count']
        print(selection)
        print(data[p2]['follower_count'])
        if selection > p2_followers:
            points += 1
        else:
            print(f"you lose. final score is {points}.")
            game_lose = True
    if selection == 'B':
        print(selection)
        selection = data[p2]['follower_count']
        print(data[p2]['follower_count'])
        if selection > p1_followers:
            points += 1
        else:
            print(f"you lose. final score is {points}.")
            game_lose = True
#check if people are not same
