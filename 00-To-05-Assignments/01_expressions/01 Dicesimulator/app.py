import random

def roll_dice():
    # These variables (die1 and die2) have local scope within roll_dice()
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    for i in range(1, 4):
        # Call the roll_dice function to get a new pair of dice results each time.
        die1, die2 = roll_dice()
        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")

if __name__ == "__main__":
    main()






