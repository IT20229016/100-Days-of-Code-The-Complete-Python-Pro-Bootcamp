import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo at the start of the game
print(logo)

# Create blanks
display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, let them know
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # If the guessed letter is not in the chosen_word, let them know and reduce a life
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        
        # Print the current stage of hangman
        print(stages[lives])

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if the user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")