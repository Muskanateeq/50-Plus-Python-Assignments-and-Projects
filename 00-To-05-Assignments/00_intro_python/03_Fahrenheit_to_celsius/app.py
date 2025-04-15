def main():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the given formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the temperature in both Fahrenheit and Celsius
    print(f"\nTemperature: {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()
