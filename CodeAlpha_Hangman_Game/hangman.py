import random

# Predefined word list (5 words only)
words = ["apple", "banana", "mango", "grapes", "orange"]

# Random word selection
secret_word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess one letter at a time (a-z)")

# Game loop
while wrong_guesses < max_attempts:
    
    # Display current word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\n" + "="*30)
    print("Word:", display_word)
    print("Attempts left:", max_attempts - wrong_guesses)
    print("="*30)
    
    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break
    
    # User input
    guess = input("Enter a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter (a-z).")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    # Store guess
    guessed_letters.append(guess)
    
    # Check correct or wrong
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Lose condition
if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The word was:", secret_word)