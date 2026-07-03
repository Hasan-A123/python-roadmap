# ====================================
# Project 7 - Password Generator
# Python Roadmap
# Generate secure random passwords
# ====================================

# Import built-in modules
# random -> choose random characters
# string -> provides predefined character sets
import random
import string


def main():

    # Program title
    print("=== PASSWORD GENERATOR ===")

    # Ask the user for the desired password length
    password_length = int(input("Enter password length: "))

    # Validate password length
    if password_length <= 0:
        print("Password length must be greater than 0")
        return
    else:
        print(f"Password length: {password_length}")

    # ====================================
    # Build the character pool
    # Lowercase letters are always included
    # More character types are added depending
    # on the user's choices below.
    # ====================================
    characters = ""
    characters += string.ascii_lowercase

    # ====================================
    # Include Uppercase Letters
    # Keep asking until the user enters
    # either 'y' or 'n'
    # ====================================
    uppercase_letters = input("Include uppercase letters? (y/n): ").lower()

    while uppercase_letters not in ("y", "n"):
        print("Please enter y or n")
        uppercase_letters = input("Include uppercase letters? (y/n): ").lower()

    # Add uppercase letters if requested
    if uppercase_letters == "y":
        characters += string.ascii_uppercase

    # ====================================
    # Include Numbers
    # ====================================
    digits = input("Include numbers? (y/n): ").lower()

    while digits not in ("y", "n"):
        print("Please enter y or n")
        digits = input("Include numbers? (y/n): ").lower()

    # Add digits if requested
    if digits == "y":
        characters += string.digits

    # ====================================
    # Include Punctuation Symbols
    # ====================================
    punctuation = input("Include punctuation symbols? (y/n): ").lower()

    while punctuation not in ("y", "n"):
        print("Please enter y or n")
        punctuation = input("Include punctuation symbols? (y/n): ").lower()

    # Add punctuation symbols if requested
    if punctuation == "y":
        characters += string.punctuation

    # ====================================
    # Generate the password
    # Start with an empty string and
    # add one random character each loop.
    # ====================================
    password = ""

    for _ in range(password_length):
        random_letter = random.choice(characters)
        password += random_letter

    # Display the completed password
    print(f"Generated Password: {password}")


# Run the program only when this file
# is executed directly.
if __name__ == "__main__":
    main()