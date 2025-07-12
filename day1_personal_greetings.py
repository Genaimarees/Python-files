def main():
    # Ask for user details
    name = input("What's your name? ")
    # Convert age input to integer (optional; keeps as string otherwise)
    age_input = input("How old are you? ")
    # Try converting to int, else keep as string
    try:
        age = int(age_input)
    except ValueError:
        age = age_input  # If non-numeric, just keep original input
    
    color = input("What's your favorite color? ")

    # Build greeting
    greeting = (
        f"Hello, {name}!" 
        f"I love u so much my dear."
    )
    print("\n" + greeting)

if __name__ == "__main__":
    main()
