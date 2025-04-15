import random

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Print the results for each die and the total
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
