def get_last_element(lst):
    # Print the last element using negative indexing
    print(lst[-1])

def main():
    # Ask the user for the number of elements in the list
    count = int(input("How many elements are in your list? "))
    
    # Create an empty list to store the elements
    lst = []
    
    # Prompt the user to input each element one at a time
    for i in range(count):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    
    # Print the last element of the list using the helper function
    print("\nThe last element in the list is:")
    get_last_element(lst)

if __name__ == "__main__":
    main()
