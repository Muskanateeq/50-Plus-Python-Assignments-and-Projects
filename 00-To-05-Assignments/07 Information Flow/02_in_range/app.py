def in_range(n, low, high):
    return low <= n <= high

# Example usage:
def main():
    print(in_range(5, 1, 10))   # True, because 5 is between 1 and 10.
    print(in_range(1, 1, 10))   # True, because 1 is equal to the lower bound.
    print(in_range(10, 1, 10))  # True, because 10 is equal to the upper bound.
    print(in_range(0, 1, 10))   # False, because 0 is below 1.
    print(in_range(11, 1, 10))  # False, because 11 is above 10.

if __name__ == "__main__":
    main()
