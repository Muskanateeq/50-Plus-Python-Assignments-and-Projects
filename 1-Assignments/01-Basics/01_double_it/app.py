def main():
    # Get the initial number from the user
    curr_value = int(input("Enter a number: "))
    
    # Continue doubling until curr_value is 100 or greater.
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")
    
    print()  # Move to the next line after finishing

if __name__ == "__main__":
    main()
