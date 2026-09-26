password = input("Enter your password: ")

score = 0
common_password = False
predictable = False
repeated_characters = False

# Common passwords
common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome"
]

# Predictable words
predictable_patterns = [
    "password",
    "admin",
    "welcome",
    "qwerty",
    "letmein"
]

print()
print("Security Checks:")
print("----------------")

# Check password length
if len(password) >= 8:
    score += 1
    print("✓ At least 8 characters")
else:
    print("✗ At least 8 characters")

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1
    print("✓ Contains uppercase letters")
else:
    print("✗ Contains uppercase letters")

# Check for lowercase letters
if any(char.islower() for char in password):
    score += 1
    print("✓ Contains lowercase letters")
else:
    print("✗ Contains lowercase letters")

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1
    print("✓ Contains numbers")
else:
    print("✗ Contains numbers")

# Check for special characters
if any(not char.isalnum() for char in password):
    score += 1
    print("✓ Contains special characters")
else:
    print("✗ Contains special characters")


# Check if password is commonly used
if password.lower() in common_passwords:
    common_password = True

    print()
    print("⚠ WARNING: This is a commonly used password.")
    print("It may be easy for attackers to guess.")


# Check for predictable patterns
password_lower = password.lower()

for pattern in predictable_patterns:
    if pattern in password_lower:
        predictable = True
        break

if predictable:
    print()
    print("⚠ WARNING: Your password contains a predictable pattern.")
    print("Avoid common words such as password, admin, welcome or qwerty.")


# Check for repeated characters
if len(password) >= 3:
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            repeated_characters = True
            break

if repeated_characters:
    print()
    print("⚠ WARNING: Your password contains repeated characters.")
    print("Avoid using the same character multiple times.")


# Decide the password rating
if common_password:
    rating = "WEAK - COMMON PASSWORD"
elif predictable:
    rating = "WEAK - PREDICTABLE"
elif repeated_characters:
    rating = "WEAK - REPEATED CHARACTERS"
elif score <= 1:
    rating = "VERY WEAK"
elif score == 2:
    rating = "WEAK"
elif score == 3:
    rating = "MEDIUM"
elif score == 4:
    rating = "STRONG"
else:
    rating = "VERY STRONG"


print()
print("==============================")
print("Password Rating:", rating)
print("Score:", score, "/ 5")
print("==============================")


# Create recommendations
recommendations = []

if len(password) < 8:
    recommendations.append("Use at least 8 characters.")

if not any(char.isupper() for char in password):
    recommendations.append("Add at least one uppercase letter.")

if not any(char.isdigit() for char in password):
    recommendations.append("Add at least one number.")

if not any(not char.isalnum() for char in password):
    recommendations.append("Add a special character such as !, @ or #.")

if common_password:
    recommendations.append(
        "Avoid common passwords that attackers can easily guess."
    )

if predictable:
    recommendations.append(
        "Avoid predictable words and patterns in passwords."
    )

if repeated_characters:
    recommendations.append(
        "Avoid repeating the same character multiple times."
    )


# Display recommendations
if recommendations:
    print()
    print("Recommendations:")
    print("----------------")

    for recommendation in recommendations:
        print("- " + recommendation)
else:
    print()
    print("✓ Your password passes all basic checks.")