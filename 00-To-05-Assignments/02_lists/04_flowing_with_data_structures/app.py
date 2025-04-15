def add_three_copies(lst, data):
    # Add three copies of data to the list
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Prompt the user for a message
    message = input("Enter a message to copy: ")

    # Create an empty list and display it before modification
    my_list = []
    print(f"\nList before: {my_list}")

    # Call the helper function to add three copies of the message to the list
    add_three_copies(my_list, message)

    # Display the list after modification
    print(f"\nList after: {my_list}")

if __name__ == "__main__":
    main()
