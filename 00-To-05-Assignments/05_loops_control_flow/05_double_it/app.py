def main():
    # Ask the user to enter a number and store it in curr_value.
    curr_value = int(input("Enter a number: "))
    
    # Double curr_value until it is 100 or greater.
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")
    
    print()  # Print a newline after the loop finishes

if __name__ == "__main__":
    main()
