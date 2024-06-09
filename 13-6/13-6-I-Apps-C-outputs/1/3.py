
def get_original_character(n, k, characters):
    # Initialize a binary string with all features set to 0
    original_character = "0" * k

    # Loop through each character and compare it to the original character
    for character in characters:
        # Calculate the similarity between the two characters
        similarity = 0
        for i in range(k):
            if character[i] == original_character[i]:
                similarity += 1

        # If the similarity is less than the current minimum similarity, update the original character
        if similarity < min_similarity:
            min_similarity = similarity
            original_character = character

    return original_character

