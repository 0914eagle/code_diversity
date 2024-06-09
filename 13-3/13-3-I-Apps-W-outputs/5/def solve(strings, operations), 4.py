
def solve(strings, operations):
    # Initialize an empty dictionary to store the concatenated strings
    concatenated_strings = {}

    # Loop through each operation
    for a, b in operations:
        # Concatenate the strings and store the result in the dictionary
        concatenated_strings[a] = concatenated_strings.get(a, "") + strings[b]

        # Make the bth string empty
        strings[b] = ""

    # Return the last string that remains
    return concatenated_strings[len(concatenated_strings)]

