import random
import string
import pyperclip
from datetime import datetime

#Password Strength Checker
def check_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6 or score <= 1:
        return "WEAK"
    elif length >= 6 and score == 2:
        return "MEDIUM"
    else:
        return "STRONG"

#Password Generator 
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Save Password to File
def save_password(password, strength):
    with open("saved_passwords.txt", "a") as file:
        file.write(f"{datetime.now()} | Password: {password} | Strength: {strength}\n")

#Main program
def main():
    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    password = generate_password(length)
    strength = check_strength(password)

    print("\nGenerated Password:", password)
    print("Password Strength:", strength)

    # Copy to clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard ✅")

    # Save to file
    save_password(password, strength)
    print("Password saved to file 📁")

if __name__ == "__main__":
    main()
