import random

# Constant for number of rounds to play.
NUM_ROUNDS = 5

def get_user_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    # Continue prompting until the input is valid.
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").lower()
    return guess

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize user score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the user and computer (between 1 and 100, inclusive).
        user_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)
        
        # Show the user their number.
        print(f"Your number is {user_num}")
        
        # Get a validated guess from the user.
        guess = get_user_guess()
        
        # Determine if the user's guess is correct:
        #   - If guess is "higher", then user wins if user_num > computer_num.
        #   - If guess is "lower", then user wins if user_num < computer_num.
        # In case the numbers are equal, the computer wins.
        if (guess == "higher" and user_num > computer_num) or (guess == "lower" and user_num < computer_num):
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        print(f"Your score is now {score}\n")
    
    # Game over; print final messages.
    print("Thanks for playing!")
    print(f"Your final score is {score} out of {NUM_ROUNDS}.")
    
    # Conditional ending messages.
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
