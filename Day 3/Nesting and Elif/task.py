print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age"))
    cost = 0
    if age < 12:
        cost = 5
        print(f"please pay ${cost}")

    elif age >= 12 and age <= 18:
        cost = 7
        print(f"please pay ${cost}")
    else:
        cost = 12
        print(f"please pay {cost}")

    want_photos = input("do you want photos")
    if want_photos == "no":
        print(f"your total cost will be {cost}")
    if want_photos == "yes":
        cost += 3
    print(f"you total cost will be {cost}")

else:
    print("Sorry you have to grow taller before you can ride.")
