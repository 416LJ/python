import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(letters)
print(letters)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_password = []
final_password = []
for letter in range(1,nr_letters + 1):
    new_password.append(random.choice(letters))
for number in range(1, nr_symbols + 1):
    new_password.append(random.choice(symbols))
for symbol in range (1, nr_numbers + 1):
    new_password.append(random.choice(numbers))
random.shuffle(new_password)
final_password = "".join(new_password)

pass2 = ""
for letter in new_password:
    pass2 += letter

print(pass2)
print(f"you new password should be:\n{final_password}")
