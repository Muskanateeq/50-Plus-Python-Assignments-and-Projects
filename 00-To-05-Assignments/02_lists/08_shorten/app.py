MAX_LENGTH = 3

def shorten(lst):
    # Remove elements from the end until the list is MAX_LENGTH items long.
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    # For demonstration, we prompt the user to enter a list of items separated by spaces.
    # The list is then passed to the shorten() function.
    user_input = input("Enter some items separated by spaces: ")
    lst = user_input.split()
    
    print("\nRemoving items:")
    shorten(lst)
    
    print("\nShortened list:", lst)

if __name__ == "__main__":
    main()
