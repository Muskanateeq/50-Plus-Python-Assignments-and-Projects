def main():
    # Create an empty dictionary to serve as the phonebook
    phonebook = {}
    
    # Prompt the user to add entries to the phonebook
    print("Enter phonebook entries. Press enter without typing a name to finish.")
    
    while True:
        name = input("Enter a name: ")
        if name == "":
            break  # Exit the loop if the user doesn't enter a name
        
        number = input(f"Enter the phone number for {name}: ")
        phonebook[name] = number  # Store the entry in the dictionary
    
    # Print the complete phonebook
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

if __name__ == "__main__":
    main()
