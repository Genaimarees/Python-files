def format_name(full_name):
    # Split the name into parts
    name_parts = full_name.strip().split()
    
    if len(name_parts) < 2:
        print("Please enter at least first and last name.")
        return
    
    first = name_parts[0]
    last = name_parts[-1]
    middle = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

    print(f"Original Name: {full_name}")
    print(f"First Last: {first} {last}")
    print(f"Last, First: {last}, {first}")
    

# Example usage
full_name = input("Enter full name: ")
format_name(full_name)
