def print_multiple(message, repeats):
    """
    Prints the provided message the specified number of times.

    Parameters:
        message (str): The message to be printed.
        repeats (int): The number of times to print the message.
    """
    for _ in range(repeats):
        print(message, end=" ")
    print()  # Move to a new line after printing

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()
