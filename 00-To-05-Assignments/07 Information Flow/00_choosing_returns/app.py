ADULT_AGE = 18

def is_adult(age):
    return age >= ADULT_AGE

def main():
    # Prompt the user for an age.
    age = int(input("How old is this person?: "))
    # Print the result of checking if the person is an adult.
    print(is_adult(age))

if __name__ == "__main__":
    main()
