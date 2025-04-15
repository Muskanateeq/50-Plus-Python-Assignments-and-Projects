def double(num):
    """
    Returns the result of multiplying num by 2.
    
    Parameters:
        num (int or float): The number to double.
        
    Returns:
        int or float: The doubled value.
    """
    return num * 2

def main():
    # Prompt the user for a number.
    num = float(input("Enter a number: "))
    # Compute the double of the number.
    result = double(num)
    # Print the result.
    print(f"Double that is {result}")

if __name__ == "__main__":
    main()
