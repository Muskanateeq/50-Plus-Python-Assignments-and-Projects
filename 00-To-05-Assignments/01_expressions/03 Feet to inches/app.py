def main():
    # Prompt the user to enter a measurement in feet
    feet = float(input("Enter the number of feet: "))
    
    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12
    
    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":
    main()

