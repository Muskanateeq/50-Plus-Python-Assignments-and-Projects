import time

def main():
    try:
        # Prompt the user for the number of seconds to count down from.
        total_seconds = int(input("Enter the number of seconds for the countdown: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print("\nCountdown begins!\n")
    
    # Count down from the specified number of seconds to 0.
    for remaining in range(total_seconds, 0, -1):
        print(f"{remaining} seconds remaining...", end="\r", flush=True)
        time.sleep(1)
    
    # Clear the line and print final message.
    print("Time's up!                        ")

if __name__ == "__main__":
    main()
