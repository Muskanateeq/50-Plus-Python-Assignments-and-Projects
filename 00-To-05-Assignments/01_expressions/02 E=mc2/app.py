def main():
    # Constant for the speed of light in m/s
    C = 299792458

    while True:
        try:
            # Prompt the user for the mass in kilograms
            mass = float(input("Enter kilos of mass: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Calculate the energy using Einstein's formula: E = m * C^2
        energy = mass * C**2
        
        # Display the results in the specified format
        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s\n")
        print(f"{energy} joules of energy!\n")

if __name__ == "__main__":
    main()
