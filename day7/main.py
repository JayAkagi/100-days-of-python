import random

word_list = ["daedalus", "butterfly", "bracer", "broadsword"]

selected_word = word_list[random.randint(0, len(word_list) - 1)]

user_guess = input("Guess a letter: ").lower()

for char in selected_word:
    if char == user_guess:
        print("Letter is in the word.")
    else:
        print(print("Letter is not in the word."))