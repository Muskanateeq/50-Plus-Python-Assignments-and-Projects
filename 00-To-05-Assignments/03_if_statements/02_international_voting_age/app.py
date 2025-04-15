def main():
    # Prompt the user for their age
    age = int(input("How old are you? "))
    
    # Define the voting ages for each country
    peturks_age = 16
    stanlau_age = 25
    mayengua_age = 48
    
    # Determine voting eligibility in Peturksbouipo
    if age >= peturks_age:
        print(f"You can vote in Peturksbouipo where the voting age is {peturks_age}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {peturks_age}.")
    
    # Determine voting eligibility in Stanlau
    if age >= stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")
    
    # Determine voting eligibility in Mayengua
    if age >= mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")

if __name__ == "__main__":
    main()
