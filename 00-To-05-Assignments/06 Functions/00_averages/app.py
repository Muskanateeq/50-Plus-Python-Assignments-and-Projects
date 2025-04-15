def average_of_two(num1, num2):
    """
    Returns the average of two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The average of num1 and num2.
    """
    return (num1 + num2) / 2

# Example usage:
if __name__ == "__main__":
    a = 10
    b = 20
    print("The average of", a, "and", b, "is", average_of_two(a, b))
