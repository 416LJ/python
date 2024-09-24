import menu


def show_resources():
    for i, item in enumerate(menu.resources):
        print(f"{item} :  {menu.resources[item]}")


def count_money(money, total_money):
    for i, item in enumerate(money):
        if item == 'quarter':
            total_money += menu.money[item] * .25
        if item == 'dime':
            total_money += menu.money[item] * .10
        if item == 'nickel':
            total_money += menu.money[item] * .05
    print(f"money : ${total_money:.2f}")


def check_resources(place_order):
    if place_order == 'latte':
        if (menu.resources['water'] > menu.MENU['latte']['ingredients']['water'] and
                menu.resources['milk'] > menu.MENU['latte']['ingredients']['milk'] and
                menu.resources['coffee'] > menu.MENU['latte']['ingredients']['coffee']):
            return True
        else:
            return False
    if place_order == 'cappuccino':
        if (menu.resources['water'] > menu.MENU['cappuccino']['ingredients']['water'] and
                menu.resources['milk'] > menu.MENU['cappuccino']['ingredients']['milk'] and
                menu.resources['coffee'] > menu.MENU['cappuccino']['ingredients']['coffee']):
            return True
        else:
            return False
    if place_order == 'espresso':
        if (menu.resources['water'] > menu.MENU['espresso']['ingredients']['water'] and
                menu.resources['coffee'] > menu.MENU['espresso']['ingredients']['coffee']):
            return True
        else:
            return False


orders = []


def coffee_maker():
    total_money = 0

    # TODO prompt user to take input
    place_order = input("what would you like? (espresso/latte/cappuccino)\nenter 'espresso' for espresso\nenter "
                        "'cappuccino'"
                        "for "
                        "cappuccino\nenter 'latte' for latte\n").lower()

    # TODO turn off the machine
    if place_order == 'off':
        exit()

    # TODO check report
    if place_order == 'report':
        show_resources()
        count_money(menu.money, total_money)
        print(f"previous orders : {orders}")
        print("\n" * 5)
        coffee_maker()

    # TODO check if resources sufficient
    if check_resources(place_order):
        print("insert coins")
        money_in = 0
        quarters = int(input("insert the # of quarters"))
        money_in += (quarters * .25)
        dimes = int(input("insert the # of dimes"))
        money_in += (dimes * .10)
        nickels = int(input("insert the # of nickels"))
        money_in += (nickels * .05)
        your_money = round(money_in, 2)

        if your_money < menu.MENU[place_order]['cost']:
            print("not enough money")
            coffee_maker()
        # TODO check transaction
        change_due = 0
        if your_money < menu.MENU[place_order]['cost']:
            print("not enough money")
        else:
            if your_money == menu.MENU[place_order]['cost']:
                if place_order == 'espresso':
                    menu.resources['water'] -= menu.MENU[place_order]['ingredients']['water']
                    menu.resources['coffee'] -= menu.MENU[place_order]['ingredients']['coffee']
                else:
                    menu.resources['milk'] -= menu.MENU[place_order]['ingredients']['milk']
                    menu.resources['water'] -= menu.MENU[place_order]['ingredients']['water']
                    menu.resources['coffee'] -= menu.MENU[place_order]['ingredients']['coffee']
                print(" coffee")
                # make coffee
            else:
                change_due = your_money - menu.MENU[place_order]['cost']
                menu.money['quarter'] += quarters
                menu.money['dime'] += dimes
                menu.money['nickel'] += nickels
                if place_order == 'espresso':
                    menu.resources['water'] -= menu.MENU[place_order]['ingredients']['water']
                    menu.resources['coffee'] -= menu.MENU[place_order]['ingredients']['coffee']
                else:
                    menu.resources['milk'] -= menu.MENU[place_order]['ingredients']['milk']
                    menu.resources['water'] -= menu.MENU[place_order]['ingredients']['water']
                    menu.resources['coffee'] -= menu.MENU[place_order]['ingredients']['coffee']
        print(f"Cash in: {your_money:.2f}")
        print(f"Cost of {place_order} : {menu.MENU[place_order]['cost']:.2f}")

        quarters_out = 0
        dimes_out = 0
        nickels_out = 0
        print(menu.money)
        if change_due > 0:
            while change_due - .25 >= 0 and menu.money['quarter'] > 0:
                print(menu.money)
                menu.money['quarter'] -= 1
                change_due -= .25
                quarters_out += 1
                change_due = round(change_due, 2)
            while change_due - .10 >= 0 and menu.money['dime'] > 0:
                print(menu.money)
                menu.money['dime'] -= 1
                change_due -= .10
                dimes_out += 1
                change_due = round(change_due, 2)
            while change_due - .05 >= 0 and menu.money['nickel'] > 0:
                print(menu.money)
                menu.money['nickel'] -= 1
                change_due -= .05
                nickels_out += 1
                change_due = round(change_due, 2)
        print(menu.money)
        total_change = (quarters_out * .25) + (dimes_out * .1) + (nickels_out * .05)
        print(
            f"total change {round(total_change, 2):.2f} is\n{quarters_out} quarters\n{dimes_out} dimes\n"
            f"{nickels_out} nickels")
        print("enjoy your drink")
        orders.append(place_order)
        coffee_maker()
    else:
        show_resources()
        print("not enough resources")
        exit()


coffee_maker()
