def main():
    # Ask the user for a number and convert it to a float
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    squared = number * number
    
    # Print the result with the required format
    print(f"\n{number} squared is {squared}")

if __name__ == "__main__":
    main()
