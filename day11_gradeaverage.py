# Input: Get 5 test marks from the user
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / 5

# Display average
print(f"\nAverage Marks: {average:.2f}")

# Determine pass or fail
if average >= 50:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")
