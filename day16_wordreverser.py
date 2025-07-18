def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    # Join them back into a sentence
    return " ".join(reversed_words)

# Example usage
input_sentence = input("Enter a sentence: ")
output = reverse_words(input_sentence)
print("Reversed words sentence:", output)
