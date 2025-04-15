def main():
    # Prompt the user for the length of each side of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter as the sum of all three sides
    perimeter = side1 + side2 + side3

    # Print the perimeter with an appropriate message
    print(f"\nThe perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()



    