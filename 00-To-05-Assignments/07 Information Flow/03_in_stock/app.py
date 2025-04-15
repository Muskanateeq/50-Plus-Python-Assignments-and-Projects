def num_in_stock(fruit):
    inventory = {
        "pear": 1000,
        "apple": 50,
        "orange": 200,
        "banana": 75
    }
    # Return the stock for the fruit (if not in inventory, return 0)
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit.
    fruit = input("Enter a fruit: ")
    
    # Call num_in_stock to get the number in stock.
    stock = num_in_stock(fruit)
    
    # Print the stock information based on the returned value.
    if stock > 0:
        print("\nThis fruit is in stock! Here is how many:\n")
        print(stock)
    else:
        print("\nThis fruit is not in stock.")

if __name__ == "__main__":
    main()
