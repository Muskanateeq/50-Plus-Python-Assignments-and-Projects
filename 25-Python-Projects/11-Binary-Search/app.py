def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # Target found, return its index
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

def main():
    # Sample sorted list for demonstration
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    print("Sorted List:", sorted_list)
    
    # Prompt the user for a target number to search for
    try:
        target = int(input("Enter a number to search for: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Perform binary search
    index = binary_search(sorted_list, target)
    
    # Print the result
    if index != -1:
        print(f"Number {target} found at index {index} in the sorted list.")
    else:
        print(f"Number {target} not found in the sorted list.")

if __name__ == "__main__":
    main()
