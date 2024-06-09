
def get_unique_character(n, k, characters):
    # Initialize a binary string with all features set to 0
    tira_character = "0" * k

    # Loop through each feature and check if it is present in any of the other characters
    for feature in range(k):
        for character in characters:
            if character[feature] == "1":
                tira_character = tira_character[:feature] + "0" + tira_character[feature + 1:]
                break

    return tira_character

