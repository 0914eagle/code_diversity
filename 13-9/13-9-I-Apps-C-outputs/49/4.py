
def get_longest_clue(taboo_strings):
    # Initialize the longest clue to be an empty string
    longest_clue = ""

    # Iterate over the taboo strings
    for taboo_string in taboo_strings:
        # Check if the current taboo string is a substring of the longest clue
        if taboo_string in longest_clue:
            # If it is, then continue to the next iteration
            continue
        # If it is not, then add it to the longest clue
        longest_clue += taboo_string

    # Return the longest clue
    return longest_clue

