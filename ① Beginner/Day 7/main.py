# Python script for Hangman game

import random
import hangman_words
import hangman_art

print(hangman_art.logo)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
completed = False
display = []
lives = 6

for num in range(len(chosen_word)):
  display.append('_')

while not completed:
  guess = input("\nGuess a letter: ").lower()

  for index in range(len(chosen_word)):
    letter = chosen_word[index]
    if guess == letter:
      display[index] = letter

  print(f"\n{' '.join(display)}")

  if guess not in chosen_word:
    print(f"\nOh no! {guess} is not in the word. You lose a life :(")
    lives -= 1
    if lives == 0:
      completed = True
      print("\nYou lose")

  if "_" not in display:
    completed = True
    print("\nYou win")

  print(hangman_art.stages[lives])
