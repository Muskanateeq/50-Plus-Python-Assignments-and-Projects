def main():
    # Prompt the user for their weight on Earth.
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Dictionary mapping each planet to its gravity factor compared to Earth.
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    # Prompt the user for the name of the planet.
    planet = input("Enter a planet: ")
    
    # Calculate the weight on the chosen planet.
    # We assume that the user always types in a valid planet with the first letter capitalized.
    equivalent_weight = earth_weight * gravity_factors[planet]
    
    # Round the result to two decimal places.
    equivalent_weight = round(equivalent_weight, 2)
    
    # Print the result.
    print(f"The equivalent weight on {planet}: {equivalent_weight}")

if __name__ == "__main__":
    main()
