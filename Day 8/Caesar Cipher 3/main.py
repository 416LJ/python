from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
go_ahead = True

def encode(original_text,shift_amount):
    original_text = text
    shift_amount = shift
    new_text = " "
    if direction == 'encode':
        for letter in text:
            if letter in alphabet:
                new_text += alphabet[((alphabet.index(letter))+shift)%(len(alphabet))]
            else:
                new_text += letter
        print(f"your encoded message is '{new_text}'")

def decode(original_text,shift_amount):
    original_text = text
    shift_amount = shift
    new_text = " "
    if direction == 'decode':
        for letter in text:
            if letter in alphabet:
                new_text += alphabet[((alphabet.index(letter))-shift)%(len(alphabet))]
            else:
                new_text += letter
        print(f"your encoded message is '{new_text}'")

def caesar(direction,text,shift):
    if direction == 'encode':
        encode(original_text=text,shift_amount=shift)
    if direction == 'decode':
        decode(original_text=text,shift_amount=shift)

while go_ahead:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    if input("go again ? ") == "yes":
        go_ahead = True
    else:
        go_ahead = False
else:
    print("goodbye")

