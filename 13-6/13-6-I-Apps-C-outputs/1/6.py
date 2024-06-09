
def get_original_character(n, k, characters):
    # Initialize a binary string with all features set to 0
    original_character = "0" * k

    # Loop through each character in the input
    for character in characters:
        # Find the features that the current character has and are not in the original character
        new_features = [i for i, f in enumerate(character) if f == "1" and original_character[i] == "0"]

        # Update the original character with the new features
        for feature in new_features:
            original_character = original_character[:feature] + "1" + original_character[feature + 1:]

    return original_character

