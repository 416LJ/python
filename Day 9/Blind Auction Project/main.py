from art import logo

print(logo)
taken_bids = {}
take_bids = True

while take_bids:
    name = input("what is your name?")
    bid = int(input("what is your bid"))
    taken_bids[name] = bid
    others = input("are there other bidders?\nPlease answer 'y' for yes.")
    print("\n" * 105)
    if others == "y":
        take_bids = True
    else:
        take_bids = False

def find_highest_bid():
    highest_bid = 0
    highest_bidder = ""

    for key in taken_bids:
        if taken_bids[key] > highest_bid:
            highest_bid = taken_bids[key]
            highest_bidder = key

    print(f"the highest bid was {highest_bid}")
    print(f"the highest bidder was {highest_bidder} with ${highest_bid} bid")

find_highest_bid()