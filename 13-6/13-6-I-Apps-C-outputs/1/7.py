
def get_unique_character(n, k, characters):
    # Initialize a binary string with all features set to 0
    tira_character = "0" * k
    # Loop through each feature
    for i in range(k):
        # Count the number of characters with feature i set to 1
        count = 0
        for character in characters:
            if character[i] == "1":
                count += 1
        # If the count is less than the number of players, set the feature to 1 for Tira's character
        if count < n:
            tira_character = tira_character[:i] + "1" + tira_character[i+1:]
    return tira_character

