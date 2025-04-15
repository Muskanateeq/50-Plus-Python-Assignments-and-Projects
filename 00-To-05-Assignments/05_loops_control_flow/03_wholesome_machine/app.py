def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    # Initial prompt
    print("Please type the following affirmation:")
    
    while True:
        # Read user input without a prompt so that the message above is displayed.
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")
            print("Please type the following affirmation:")

if __name__ == "__main__":
    main()
