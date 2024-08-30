enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
    drink_potion()

game()


player_health = 10
