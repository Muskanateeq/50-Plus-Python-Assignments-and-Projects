def main():
    # Read a year from the user and convert it to an integer
    year = int(input("Enter a year: "))
    
    # Check if the year is a leap year using the Gregorian calendar rules:
    # 1. The year must be divisible by 4;
    # 2. If the year is divisible by 100, it is NOT a leap year, unless;
    # 3. The year is also divisible by 400, then it is a leap year.
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == "__main__":
    main()
