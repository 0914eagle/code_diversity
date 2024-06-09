
def solve(N, taboo_strings):
    # Initialize the longest valid string as an empty string
    longest_valid_string = ""

    # Iterate over the taboo strings
    for taboo_string in taboo_strings:
        # Check if the current taboo string is a prefix of the longest valid string
        if taboo_string in longest_valid_string:
            # If it is, replace the longest valid string with the current taboo string
            longest_valid_string = taboo_string

    # Return the longest valid string
    return longest_valid_string

