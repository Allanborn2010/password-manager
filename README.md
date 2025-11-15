# Password Manager 🔒

A simple but secure password management tool built in Python. This project demonstrates:

- Secure storage of passwords using **Fernet symmetric encryption**.
- Master password authentication with **SHA256 hashing**.
- File-based storage of encrypted passwords.
- User-friendly command-line interface for saving and viewing passwords.

---

## Features

1. **Master Password**
   - First-time users set a master password.
   - Subsequent uses require authentication.
   - Passwords are hashed with SHA256 for security.

2. **Save Passwords**
   - Save multiple passwords securely.
   - Passwords are encrypted using Fernet before being written to disk.

3. **View Passwords**
   - Decrypt and view saved passwords in a readable format.
   - Only accessible after master password authentication.

4. **Exit**
   - Clean exit from the application.