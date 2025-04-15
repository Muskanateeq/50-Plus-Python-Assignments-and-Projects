def print_divisors(num):
    """
    Prints all divisors of num (i.e., all numbers from 1 to num inclusive 
    that divide num without a remainder).
    """
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  # Print a newline after printing all divisors

def main():
    number = int(input("Enter a number: "))
    print_divisors(number)

if __name__ == "__main__":
    main()
