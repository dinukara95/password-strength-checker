# Password Strength Checker 🔐

A simple Python-based password security checker that evaluates a password using several basic security rules.

This project was created as a beginner cybersecurity project to practice Python programming and understand some basic password security concepts.

## Features

The program checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common passwords
- Predictable password patterns
- Repeated characters

It then:

- Gives the password a score out of 5
- Provides a password rating
- Shows security warnings
- Gives recommendations for improving the password

## Example

```text
Enter your password: Password123!

Security Checks:
----------------
✓ At least 8 characters
✓ Contains uppercase letters
✓ Contains lowercase letters
✓ Contains numbers
✓ Contains special characters

⚠ WARNING: Your password contains a predictable pattern.
Avoid common words such as password, admin, welcome or qwerty.

==============================
Password Rating: WEAK - PREDICTABLE
Score: 5 / 5
==============================

Recommendations:
----------------
- Avoid predictable words and patterns in passwords.