def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage:
if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5]
    result = sum_of_numbers(sample_numbers)
    print(f"The sum of {sample_numbers} is {result}.")
