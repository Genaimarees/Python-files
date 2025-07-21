def shift_by_one(word):
    shifted = ""
    for char in word:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character by 1 and wrap around using modulo 26
            shifted += chr((ord(char) - base + 1) % 26 + base)
        else:
            shifted += char  # Keep punctuation, space, etc.
    return shifted

# Example usage
if __name__ == "__main__":
    text = input("Enter a word or sentence: ")  # Example: "hello"
    shifted_text = shift_by_one(text)
    print("Shifted by 1:", shifted_text)
