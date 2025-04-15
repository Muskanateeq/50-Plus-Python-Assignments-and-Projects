def main():
    # Dictionary mapping fruit names to their prices
    fruits = {
        "apple": 3.0,      # 2 apples cost 2 * 3.0 = 6.0
        "durian": 5.0,     # not purchased in the sample run
        "jackfruit": 9.0,  # 1 jackfruit costs 9.0
        "kiwi": 2.5,       # not purchased in the sample run
        "rambutan": 11.0,  # 1 rambutan costs 11.0
        "mango": 24.5      # 3 mangoes cost 3 * 24.5 = 73.5
    }
    
    total = 0  # Initialize total cost to zero
    
    # Loop through each fruit in the dictionary and ask the user for a quantity.
    for fruit, price in fruits.items():
        quantity_str = input(f"How many ({fruit}) do you want?: ")
        quantity = int(quantity_str)  # Convert input to an integer
        total += quantity * price     # Multiply the quantity by the fruit's price and add to total
        
    # Print the final total cost.
    print(f"\nYour total is ${total}")

if __name__ == "__main__":
    main()
