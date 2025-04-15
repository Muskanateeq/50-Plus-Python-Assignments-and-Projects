def main():
    MAX_VALUE = 10000  # Constant for the maximum value
    
    a, b = 0, 1  # Starting values for Fibonacci sequence
    # Print terms until a reaches MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b  # Update the values for the next term
    print()  # Move to a new line after printing all terms

if __name__ == "__main__":
    main()
