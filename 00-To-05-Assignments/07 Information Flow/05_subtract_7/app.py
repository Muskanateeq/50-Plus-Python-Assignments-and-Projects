def subtract_seven(num):
    """
    Subtracts 7 from num and returns the result.
    """
    return num - 7

def main():
    # Prompt the user for a number.
    num = float(input("Enter a number: "))
    # Call subtract_seven to compute the result.
    result = subtract_seven(num)
    # Print the result.
    print("The result after subtracting 7 is:", result)

if __name__ == "__main__":
    main()
