import random
from word_list import words

Total_lives = 6

# Generates random word from the word list file and length of the word
chosen_word = random.choice(words)
print(chosen_word)
length = len(chosen_word)

# creates the "_" of word length and saves it to placeholder
place_holder = ""
for ltr in range(length):
    place_holder += " _ "
print(f"Word To Guess : {place_holder}") 

# Loop through until user guess the word or total_lives becomes 0 each correct letter will be saved to correct_letter list
game_over = False
correct_letters = []

while not game_over:
    print(f"You Have {Total_lives}/6 left")
    guessed_ltr = input("Guess a letter in the word: ").lower()

    if guessed_ltr in correct_letters:
        print(f"You have already guessed it {guessed_ltr}")

    display = ""

    for letter in chosen_word:
        if letter == guessed_ltr:
            display += letter
            correct_letters.append(guessed_ltr)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess :" +display)

    if guessed_ltr not in chosen_word:
        Total_lives -= 1
        print(f"You guessed {guessed_ltr} thats not in the word. You lose a life")

    if Total_lives == 0:
        game_over = True
        print(f"IT WAS {chosen_word} ! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("YOU WIN")

print(Total_lives) 


