import random

# For this example, we define DONE_LIKELIHOOD to simulate a chance to stop.
DONE_LIKELIHOOD = 0.3  # For instance, a 30% chance to be "done" before printing the next number.

def done():
    """
    Returns True with a likelihood of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Counts from 1 to 10, but before printing each number,
    checks if done() returns True. If it does, the function returns immediately.
    """
    for i in range(1, 11):
        if done():
            return  # Stop counting if done() returns True.
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
