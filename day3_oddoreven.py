def check_parity(num):
    # Using modulo operator (%)
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_parity_bitwise(num):
    # Using bitwise AND (&)
    return "Even" if (num & 1) == 0 else "Odd"

def main():
    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("❌ That's not a valid whole number.")
        return

    result_mod = check_parity(n)
    result_bit = check_parity_bitwise(n)

    print(f"→ Using %.2 modulus: {n} is {result_mod}")
    print(f"→ Using bitwise &: {n} is {result_bit}")

if __name__ == "__main__":
    main()
