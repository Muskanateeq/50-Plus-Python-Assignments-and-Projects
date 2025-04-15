import math

def main():
    # Prompt the user for the lengths of sides AB and AC
    side_ab = float(input("Enter the length of AB: "))
    side_ac = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse (BC) using the Pythagorean theorem: BC = sqrt(AB**2 + AC**2)
    hypotenuse = math.sqrt(side_ab ** 2 + side_ac ** 2)
    
    # Print the result in the specified format
    print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse}")

if __name__ == "__main__":
    main()


