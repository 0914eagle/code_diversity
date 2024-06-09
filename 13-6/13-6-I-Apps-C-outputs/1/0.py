
def get_original_character(n, k, characters):
    # Initialize a binary string with all features set to 0
    original_character = "0" * k

    # Loop through each character in the input
    for character in characters:
        # Find the features that the current character has and are not present in the original character
        features = [i for i, c in enumerate(character) if c == "1" and original_character[i] == "0"]

        # Set the features that the current character has and are not present in the original character to 1 in the original character
        for feature in features:
            original_character = original_character[:feature] + "1" + original_character[feature + 1:]

    return original_character

