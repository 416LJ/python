import random
import hangman_art
import hangman_words

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blank_word = ""
blank_array =[]
display = ""

for i in range(1,word_length+1):
    blank_word += "_"
    blank_array.append("-")

word_in_array = []
for letter in chosen_word:
    word_in_array.append(letter)
stages = -1
lives = 7
while lives > 0:
    print(f"Number of lives remaining {lives}\n")
    print(f"your word is {blank_array}")
    print(display)
    user_choice = input("\n Please guess a letter..")
    user_choice = user_choice.lower()

    letter_index = len(chosen_word)

    for letter in chosen_word:
        if letter == user_choice:
            display+= letter
        else:
            display += "_"

    if user_choice in word_in_array:
        print(f"the letter '{user_choice}' is in the word\n")
        for i in range(letter_index):
            if user_choice == word_in_array[i]:
                blank_array[i] = user_choice
    if blank_array == word_in_array:
        break
    if user_choice not in word_in_array:
        print(f"sorry you guessed a wrong letter '{user_choice}'\n")
        lives -= 1
        print(hangman_art.stages[stages])
        stages -= 1

print("game over")





