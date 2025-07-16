# listmaximum.py

# A list of numbers
numbers = [110, 45, 110, 89, 23, 78, 90, 34]

# Step 1: Assume the first element is the largest
largest = numbers[0]

# Step 2: Loop through the list
for num in numbers:
    if num > largest:
        largest = num

# Step 3: Print the result
print("The largest number in the list is:", largest)
