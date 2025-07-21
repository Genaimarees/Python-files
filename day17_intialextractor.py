def get_initials(full_name):
    # Split the name into words
    name_parts = full_name.strip().split()

    # Take the first letter of each word, capitalize it
    initials = ''.join(part[0].upper() for part in name_parts if part)

    return initials


# Example usage
if __name__ == "__main__":
    full_name = input("Enter full name: ")  # e.g., "john doe smith"
    print("Initials:", get_initials(full_name))  # Output: "JDS"
