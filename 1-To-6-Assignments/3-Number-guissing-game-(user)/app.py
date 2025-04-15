def main():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    print("For each guess, respond with:")
    print("  'low' if my guess is too low,")
    print("  'high' if my guess is too high,")
    print("  'correct' if I guessed it right.\n")
    
    # Set initial boundaries.
    low = 1
    high = 100
    input("Once you've thought of a number, press Enter to continue...")

    while True:
        # Computer makes a guess using the midpoint.
        guess = (low + high) // 2
        response = input(f"Is your number {guess}? ").lower()
        
        if response == "correct":
            print(f"Yay! I guessed your number: {guess}")
            break
        elif response == "low":
            low = guess + 1  # The number is higher than guess.
        elif response == "high":
            high = guess - 1  # The number is lower than guess.
        else:
            print("Invalid response. Please type 'low', 'high', or 'correct'.")

if __name__ == "__main__":
    main()
