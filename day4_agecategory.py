def classify_age(age):
    if age < 0:
        return "Invalid age entered."
    elif age <= 1:
        return "Infant"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

try:
    age_input = int(input("Enter the person's age: "))
    category = classify_age(age_input)
    print(f"The person is categorized as: {category}")
except ValueError:
    print("Please enter a valid integer for age.")

