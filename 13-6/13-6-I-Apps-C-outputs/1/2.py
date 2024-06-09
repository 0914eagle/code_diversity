
def get_original_character(n, k, characters):
    # Initialize a binary string with all bits set to 1
    original_character = "1" * k
    for character in characters:
        # Find the bitwise AND of the current character and the original character
        similar_character = "".join(str(int(a) & int(b)) for a, b in zip(original_character, character))
        # Update the original character with the bitwise AND
        original_character = similar_character
    return original_character

