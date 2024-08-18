print("Welcome to Python Pizza Deliveries!")
cost = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    if pepperoni == "Y":
        cost += 17
    if pepperoni == "N":
        cost += 15
    if extra_cheese == "Y":
        cost += 1
if size == "M":
    if pepperoni == "Y":
        cost += 23
    if pepperoni == "N":
        cost += 20
    if extra_cheese == "Y":
        cost += 23
if size == "L":
    if pepperoni == "Y":
        cost += 28
    if pepperoni == "N":
        cost += 25
    if extra_cheese == "Y":
        cost += 1

print(f"Your final bill is: ${cost}." )
