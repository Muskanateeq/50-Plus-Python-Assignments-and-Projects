def greet(name):
    print("Greetings", name + "!")

def main():
    # Prompt the user for their name.
    name = input("What's your name? ")
    # Call greet() to print the greeting.
    greet(name)

if __name__ == "__main__":
    main()
