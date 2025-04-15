def count_even(lst):
    # Populate the list by prompting the user for integers.
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Count the number of even numbers in the list.
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    # Print the count of even numbers.
    print(even_count)

def main():
    # Initialize an empty list.
    numbers = []
    # Call count_even to populate the list and print the count of even numbers.
    count_even(numbers)

if __name__ == "__main__":
    main()
