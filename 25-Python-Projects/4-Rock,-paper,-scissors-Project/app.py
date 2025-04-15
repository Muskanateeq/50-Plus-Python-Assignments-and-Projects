import random

def get_computer_choice():
    """Randomly select and return 'rock', 'paper', or 'scissors'."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user and computer choices.
    
    Returns:
        "tie" if both choices are the same,
        "user" if the user wins,
        "computer" if the computer wins.
    """
    if user_choice == computer_choice:
        return "tie"
    
    if user_choice == "rock":
        return "user" if computer_choice == "scissors" else "computer"
    elif user_choice == "paper":
        return "user" if computer_choice == "rock" else "computer"
    elif user_choice == "scissors":
        return "user" if computer_choice == "paper" else "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Game loop: continue playing until the user decides to quit.
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        # Validate user input.
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine and display the winner.
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
        else:
            print("Computer wins!")
        
        # Ask if the user wants to play again.
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
