# count_vowels.py

# Get input from the user
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for char in word:
    if char in vowels:
        count += 1

# Print the result
print("Number of vowels in the word:", count)
