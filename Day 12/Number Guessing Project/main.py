from random import randint
from select import select

logo = '''
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ /
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       
'''

print(logo)
EASY_LIVES = 10
HARD_LIVES = 5

def check_answer(user_guess, answer, turns):
    if user_guess == answer:
        return "winner"
    elif user_guess < answer:
        return turns -1
    else:
        return turns -1

def set_difficulty():
    difficulty = input("choose 'e' for easy and 'h' for hard.")
    if difficulty == 'e':
        return EASY_LIVES
    elif difficulty == 'h':
        return HARD_LIVES
    else:
        return

def game():
    print("Welcome to the guessing game\nIm thinking of a number between 1 and 100")
    random_number = randint(1,100)
    print(f"test number is : {random_number}")
    turns = set_difficulty()

    while turns is None:
        print("invalid entry")
        turns = set_difficulty()

    guess = 0
    while guess != random_number:
        print(f"you have {turns} left.")
        try:
            guess = int(input("guess a number: "))
        except ValueError:
            print("invalid entry, enter a number")
            guess = int(input("guess a number: "))
        print(f"you guessed {guess}")
        turns = check_answer(guess,random_number,turns)
        if turns == 0:
            print(f"you have {turns} lives. GAME OVER")
            return

game()
