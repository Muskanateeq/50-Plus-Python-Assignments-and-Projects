def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create a funny story.")

    # Getting user input
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    food = input("Enter a type of food: ")

    # Mad Libs story
    story = f"""
    One day, {name} went to {place}. 
    There, they saw a {adjective} {animal} that was trying to {verb} a {food}.
    Everyone in {place} was amazed, and {name} couldn't stop laughing!
    What a crazy day it was!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs game
mad_libs()
