
def solve(strings, operations):
    # Initialize an empty dictionary to store the concatenated strings
    concatenated_strings = {}

    # Iterate through the operations
    for a, b in operations:
        # Concatenate the strings and store the result in the dictionary
        concatenated_strings[a] = concatenated_strings.get(a, "") + strings[b]

        # Empty the string at index b
        strings[b] = ""

    # Return the last string that remains
    return concatenated_strings[len(concatenated_strings)]

