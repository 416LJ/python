import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    print(logo)
    your_cards = []
    comp_cards = []

    def replay():
        replays = input("want to play again? 'y' or 'n'.")
        if replays == 'y':
            blackjack()
        else:
            print("thank you for playing")
            exit()

    def your_total():
        total = 0
        your_cards2 = sorted(your_cards)
        for i in your_cards2:
            if total >= 11 and i == 11:
                total = total + 1
            else:
                total = total + i
        return total

    def comp_total():
        total = 0
        comp_cards2 = sorted(comp_cards)
        for i in comp_cards2:
            if total >= 11 and i == 11:
                total = total + 1
            else:
                total = total + i
        return total

    your_first_card = random.choice(cards)
    your_cards.append(your_first_card)
    your_2nd_card = random.choice(cards)
    your_cards.append(your_2nd_card)
    print(f"your total is {your_cards} : {your_total()}")

    comp_first_card = random.choice(cards)
    comp_cards.append(comp_first_card)
    comp_2nd_card = random.choice(cards)
    comp_cards.append(comp_2nd_card)
    print(f"comp total is {comp_cards} : {comp_total()}")

    if your_total() == 21:
        return print("BlackJack, you win")
    elif comp_total() == 21:
        return print("BlackJack, you lose")
    else:
        choice = 'h'
        while choice == 'h' and your_total() < 21:
            choice = input("hit or stay? Press H or S")
            if choice == 's':
                choice = 's'
            if choice == 'h':
                card = random.choice(cards)
                your_cards.append(card)
                print(your_cards)
                print(your_total())
            if your_total() == 21:
                print("BlackJack, you win")
                replay()
            if your_total() > 21:
                print("you lose")
                replay()

        print("computers turn now")

        if comp_total() > your_total():
            print("you lose")
            replay()
        elif comp_total() == your_total():
            print("tie")
            replay()

        while comp_total() < 17 and not comp_total() >21:
            card = random.choice(cards)
            comp_cards.append(card)
            print(comp_cards)
            print(comp_total())
            if comp_total() > 21:
                print("you win")
                replay()
        if comp_total() == 21:
            print("blackjack, you lose")
        elif your_total() > comp_total():
            print("you win")
            replay()
        elif comp_total() == your_total():
            print("tie")
            replay()
        else:
            print("you lose")
            replay()

blackjack()


