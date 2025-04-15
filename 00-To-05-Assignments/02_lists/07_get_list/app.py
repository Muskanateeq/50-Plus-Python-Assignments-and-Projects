def main():
    values = []  # Initialize an empty list

    while True:
        # Prompt the user for input
        value = input("Enter a value: ")
        
        # If the user just presses enter (empty input), break out of the loop
        if value == "":
            break
        
        # Append the value (as a string) to the list
        values.append(value)
    
    # Print the resulting list
    print("\nHere's the list:", values)

if __name__ == "__main__":
    main()
