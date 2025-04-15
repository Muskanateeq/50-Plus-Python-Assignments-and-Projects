def list_practice():
    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Initial fruit list:", fruit_list)
    print("Length of the fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)
    print("-" * 40)


def access_element(lst, index):
    """Returns the element at the specified index."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Error: Index out of range."


def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} updated to '{new_value}'."
    else:
        return "Error: Index out of range."


def slice_list(lst, start, end):
    """Returns a sublist from start to end index."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Error: Invalid index range."


def index_game():
    my_list = ["apple", "banana", "cherry", "date", "fig", "grape"]

    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1 - Access an element")
        print("2 - Modify an element")
        print("3 - Slice the list")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print("Result:", access_element(my_list, index))
        
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print("Result:", modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == "4":
            print("Exiting game.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the programs
list_practice()
index_game()
