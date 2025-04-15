import random

def main():
    # Computer selects a secret number between 1 and 100.
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses correctly.
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed correctly. The number was: {secret_number}")
            break

if __name__ == "__main__":
    main()

