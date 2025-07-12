# Count positive, negative, and zero numbers in a list

# Sample list
numbers = [3, -1, 0, 7, -5, 0, 4, -2]

# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

# Loop through the list
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Print the results
print("📊 Number Summary:")
print(f"✅ Positive numbers: {positive_count}")
print(f"❌ Negative numbers: {negative_count}")
print(f"⭕ Zero values: {zero_count}")
