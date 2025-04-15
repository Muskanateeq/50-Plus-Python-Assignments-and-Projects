import random

# List of words for the game.
WORD_LIST = [
    "python", "hangman", "programming", "challenge", "developer",
    "algorithm", "function", "variable", "iteration", "condition"
]

# Hangman stages (from 0 wrong guesses to maximum wrong guesses)
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

MAX_WRONG = len(HANGMAN_PICS) - 1  # Maximum wrong guesses allowed.

def choose_word():
    """Randomly choose and return a word from the WORD_LIST."""
    return random.choice(WORD_LIST)

def display_board(missed_letters, correct_letters, secret_word):
    """Display the current state of the hangman and the secret word with guessed letters."""
    print(HANGMAN_PICS[len(missed_letters)])
    print("\nMissed letters:", " ".join(missed_letters))
    
    # Create a string that shows the secret word with underscores for letters not yet guessed.
    blanks = ["_" if letter not in correct_letters else letter for letter in secret_word]
    print(" ".join(blanks))
    print()

def get_guess(already_guessed):
    """Prompt the player to enter a letter. Ensures the guess is a single, new alphabetical letter."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You've already guessed that letter. Try again.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    """Return True if the player wants to play again."""
    return input("Do you want to play again? (yes or no): ").lower().startswith("y")

def main():
    print("Welcome to Hangman!")
    
    # Game loop.
    while True:
        secret_word = choose_word()
        missed_letters = []
        correct_letters = []
        game_over = False
        
        # Loop until the game is over.
        while not game_over:
            display_board(missed_letters, correct_letters, secret_word)
            guess = get_guess(missed_letters + correct_letters)
            
            if guess in secret_word:
                correct_letters.append(guess)
                
                # Check if the player has won.
                found_all_letters = all(letter in correct_letters for letter in secret_word)
                if found_all_letters:
                    print(f"Yes! The secret word is '{secret_word}'! You have won!")
                    game_over = True
            else:
                missed_letters.append(guess)
                
                # Check if player has reached the maximum number of wrong guesses.
                if len(missed_letters) == MAX_WRONG:
                    display_board(missed_letters, correct_letters, secret_word)
                    print(f"You have run out of guesses! The word was '{secret_word}'.")
                    game_over = True
        
        # Ask the player if they want to play again.
        if not play_again():
            break

if __name__ == "__main__":
    main()
