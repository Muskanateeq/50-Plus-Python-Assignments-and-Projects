import random
import string

def generate_password(length):
    """
    Generate a random password of a given length.
    
    The password is composed of uppercase letters, lowercase letters,
    digits, and punctuation characters.
    """
    # Define the characters to choose from.
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from all_characters.
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        # Ask the user for the desired password length.
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate and display the password.
    password = generate_password(length)
    print("\nGenerated password:", password)

if __name__ == "__main__":
    main()
