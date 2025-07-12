# compare_numbers.py

# Take two number inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}.")
else:
    print(f"{num1} and {num2} are equal.")
