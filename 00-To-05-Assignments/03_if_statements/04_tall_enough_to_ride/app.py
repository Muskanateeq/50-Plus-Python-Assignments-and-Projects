MIN_HEIGHT = 50

def tall_enough_extension():
    while True:
        height_str = input("How tall are you? ")
        
        # If the user enters nothing, break the loop and stop the program.
        if height_str == "":
            break
        
        # Convert the input to a number (float, to support decimals)
        height = float(height_str)
        
        # Check if the height meets the minimum requirement
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
            
def main():
    tall_enough_extension()

if __name__ == "__main__":
    main()
