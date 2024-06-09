
def get_unique_character(n, k, characters):
    # Initialize a binary string of length k with all bits set to 0
    unique_character = "0" * k

    # Iterate over the characters of the other players
    for character in characters:
        # Find the features that are common to all characters
        common_features = "".join(c for c in unique_character if c == character[c])

        # Update the unique character by setting the common features to 0
        unique_character = unique_character.replace(common_features, "0")

    return unique_character

