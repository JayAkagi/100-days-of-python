import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["daedalus", "butterfly", "bracer", "broadsword"]
display = []

selected_word = word_list[random.randint(0, len(word_list) - 1)]
player_lives = 6
win = False

for i in range(len(selected_word)):
    display.append("_")

while player_lives != 0:
    print(stages[player_lives])
    print(player_lives)
    print(f"Complete the word: {''.join(display)}")
    user_guess = input("Guess a letter: ").lower()
    turn_ok = False

    for i in range(len(selected_word)):
        char = selected_word[i]
        if char == user_guess:
            display[i] = char
            turn_ok = True

    if not turn_ok:
        player_lives -= 1

if "_" not in display:
    win = "True"

if win:
    print("You win!")
else:
    print(stages[player_lives])
    print(f"You Lose. The word was: {selected_word}")
