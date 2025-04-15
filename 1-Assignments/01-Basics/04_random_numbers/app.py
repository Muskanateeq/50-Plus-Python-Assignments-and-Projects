import random

def main():
    # Loop 10 times to generate and print 10 random numbers
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
    print()  # Print a newline at the end

if __name__ == "__main__":
    main()
