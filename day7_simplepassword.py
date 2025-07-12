# Simple password check based on minimum length

# Set the minimum length
MIN_LENGTH = 8

# Get password input from user
password = input("🔐 Enter your password: ")

# Check password length
if len(password) >= MIN_LENGTH:
    print("✅ Password is accepted.")
else:
    print("❌ Password is too short. It must be at least", MIN_LENGTH, "characters long.")
