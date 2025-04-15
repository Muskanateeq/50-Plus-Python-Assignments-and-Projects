def get_first_element(lst):
    # Since the list is guaranteed to be non-empty, we print the first element.
    print(lst[0])

def main():
    # Ask the user for the number of elements they want to input
    count = int(input("How many elements are in your list? "))
    
    # Create an empty list
    lst = []
    
    # Prompt the user to input each element one at a time
    for i in range(count):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    
    # Print the first element of the list using the helper function
    print("\nThe first element in the list is:")
    get_first_element(lst)

if __name__ == "__main__":
    main()
