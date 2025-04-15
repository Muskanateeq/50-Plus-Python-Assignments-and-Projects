def main():
    counts = {}  # Dictionary to store number counts
    
    # Continuously ask for input until the user enters nothing
    while True:
        num_str = input("Enter a number: ")
        if num_str == "":
            break
        
        # Convert the input to an integer
        num = int(num_str)
        
        # Increment the count for this number in the dictionary
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Print the results
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    main()
