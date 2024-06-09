
def solve(n, k, characters):
    # Initialize the feature vector for Tira's character
    tira_features = [0] * k

    # Iterate over the existing characters
    for character in characters:
        # Calculate the similarity between Tira's character and the current character
        similarity = 0
        for i in range(k):
            if character[i] == tira_features[i]:
                similarity += 1

        # If the similarity is lower than the current minimum similarity, update the minimum similarity and the features of Tira's character
        if similarity < min_similarity:
            min_similarity = similarity
            tira_features = character

    # Return the features of Tira's character
    return "".join(str(feature) for feature in tira_features)

