import random

word_list = ["daedalus", "butterfly", "bracer", "broadsword"]
display = []

selected_word = word_list[random.randint(0, len(word_list) - 1)]

user_guess = input("Guess a letter: ").lower()

for blank in range(len(selected_word)):
    display.append("_")

for index in range(len(selected_word)):
    char = selected_word[index]
    if char == user_guess:
        display[index] = char

print(f" Complete the word: {''.join(display)}")