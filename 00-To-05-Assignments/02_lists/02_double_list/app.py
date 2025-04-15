def double_elements(numbers):
    # Iterate over the list using index and double each element
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def main():
    # Starting list
    numbers = [1, 2, 3, 4]
    
    # Double each element in the list
    doubled_numbers = double_elements(numbers)
    
    # Print the result
    print(doubled_numbers)

if __name__ == "__main__":
    main()
