# A Simple Password Manager

# Libraries

import os
import hashlib
import base64
from cryptography.fernet import Fernet

# File names

MASTER_FILE = "master.txt"
PASSWORDS_FILE = "passwords.txt"

# Variables to store multiple saved passwords

SavedPasswords = []

# Checks if there are already passwords saved in passwords.txt and loads them

if os.path.exists(PASSWORDS_FILE):
    with open(PASSWORDS_FILE, "rb") as f:
        SavedPasswords = [line.strip() for line in f.readlines()]

# Welcome message

print(f"Welcome to the Password Manager!")

# Check if master password exists
if os.path.exists(MASTER_FILE):
    # Load hashed master password
    with open(MASTER_FILE, "r") as f:
        HashedMasterPassword = f.read().strip()

    # Ask user to enter master password
    entered = input("Enter the master password: ")
    if hashlib.sha256(entered.encode()).hexdigest() != HashedMasterPassword:
        print("Incorrect password. Access denied.")
        exit()

    print("Access granted!")

else:
    # Create a new master password
    MasterPasswordEntered = input("Please pick your master password: ")
    HashedMasterPassword = hashlib.sha256(MasterPasswordEntered.encode()).hexdigest()

    # Save hashed master password
    with open(MASTER_FILE, "w") as f:
        f.write(HashedMasterPassword)

    print("Master password created! You are now logged in.")
    entered = MasterPasswordEntered  # use it to generate encryption key

# Generate Fernet key from the master password entered
key = hashlib.sha256(entered.encode()).digest()
fernet_key = base64.urlsafe_b64encode(key)
fernet = Fernet(fernet_key)

# Main loop for password management

while True:
    try:
        UsersChoice = int(input(f"Do you want to (1) Save a new password, (2) View saved passwords, or (3) Exit? Enter 1, 2 or 3: "))
    except ValueError:
        print(f"Please enter a number (1, 2 or 3).")
        continue

    if UsersChoice == 1:
        NewPassword = input("Enter the new password to save: ")
        # Encrypt the password
        encrypted = fernet.encrypt(NewPassword.encode())
        SavedPasswords.append(encrypted)
        # Save to file (as string)
        with open(PASSWORDS_FILE, "ab") as f:  # binary mode
            f.write(encrypted + b"\n")
        print("Password saved successfully!")

    elif UsersChoice == 2:
        if not SavedPasswords:
            print("No passwords saved yet.")
        else:
            print("Saved Passwords:")
            for i, enc_pass in enumerate(SavedPasswords, 1):
                try:
                    # Decrypt password
                    dec_pass = fernet.decrypt(enc_pass).decode()
                    print(f"{i}. {dec_pass}")
                except:
                    print(f"{i}. [Unable to decrypt]")

    elif UsersChoice == 3:
        print(f"Exiting the Password Manager. Goodbye!")
        exit()

    else:
        print(f"Invalid option. Please enter 1, 2 or 3.")
