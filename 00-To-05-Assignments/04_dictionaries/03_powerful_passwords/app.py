import hashlib

def hash_password(password):
    """
    Hashes the provided password using SHA256 and returns the hexadecimal digest.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the hash of the password_to_check matches the stored hash for the given email.
    
    Parameters:
        email (str): The user's email.
        password_to_check (str): The password the user is attempting to log in with.
        stored_logins (dict): A dictionary mapping emails to hashed passwords.
        
    Returns:
        bool: True if the hash of password_to_check matches the stored hash; False otherwise.
    """
    # Hash the password to check using the provided hash_password function.
    hashed_attempt = hash_password(password_to_check)
    
    # Get the stored hash for the given email (or None if the email isn't found).
    stored_hash = stored_logins.get(email)
    
    # Return True if the hashes match, False otherwise.
    return hashed_attempt == stored_hash

def main():
    # Example stored logins dictionary with emails as keys and hashed passwords as values.
    stored_logins = {
        "user1@example.com": hash_password("password123"),
        "user2@example.com": hash_password("mySecret!"),
    }
    
    # Simulate a login attempt.
    email = input("Enter your email: ")
    password_to_check = input("Enter your password: ")
    
    if login(email, password_to_check, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == "__main__":
    main()

