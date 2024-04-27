import random

# List of words to choose from
word_list = ["apple", "pear", "paper", "pen"]

# List to keep track of guessed letters
guessed_letters = []

# Randomly select a word from the list
word_to_guess = random.choice(word_list)

# Initialize the control variable with dashes, indicating unguessed letters
control = "-" * len(word_to_guess)

# Number of remaining attempts
lives = 6

# Loop until the player runs out of attempts or guesses the word
while lives > 0:
    # Prompt the user to input a letter
    letter = input("Enter a letter: ")

    # Flag to check if the guessed letter is found in the word
    found_letter = False

    # Check if the guessed letter is in the word
    for i in range(len(word_to_guess)):
        if letter == word_to_guess[i]:
            # If the letter is found, update the control variable
            control = control[:i] + letter + control[i + 1:]
            found_letter = True

    # Check if the guessed letter was not found in the word
    if not found_letter:
        # If the letter hasn't been guessed before, add it to the guessed letters list
        if letter not in guessed_letters:
            guessed_letters.append(letter)
        # Print the incorrect guess and the list of guessed letters
        print("Wrong guess!", guessed_letters)
        # Decrease the number of remaining attempts
        lives -= 1

    # Print the current state of the word with guessed letters
    print(control)

    # Check if the word has been completely guessed
    if "-" not in control:
        print("Congratulations! You've guessed the word:", word_to_guess)
        break

# If the player runs out of attempts, print the correct word
if lives == 0:
    print("Sorry, you're out of lives. The correct word was:", word_to_guess)
