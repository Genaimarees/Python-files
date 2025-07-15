# sum_calculator.py

# Ask user to enter a number
n = int(input("Enter a number (n): "))

# Initialize sum
total = 0

# Use a loop to calculate sum from 1 to n
for i in range(1, n + 1):
    total += i

# Print the result
print(f"The sum of numbers from 1 to {n} is: {total}")
