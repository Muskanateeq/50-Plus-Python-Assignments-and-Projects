import random

def main():
    # Generate a random number between 0 and 99 (inclusive)
    number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")
    
    # Initial guess prompt
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses correctly
    while guess != number:
        if guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        # Prompt for a new guess
        guess = int(input("\nEnter a new number: "))
    
    # When the guess is correct, congratulate the user
    print(f"Congrats! The number was: {number}")

if __name__ == "__main__":
    main()
