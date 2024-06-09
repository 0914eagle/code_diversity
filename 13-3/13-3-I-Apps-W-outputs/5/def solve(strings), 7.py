
def solve(strings):
    # Initialize an empty dictionary to store the concatenated strings
    concatenated_strings = {}

    # Iterate through the operations
    for operation in operations:
        # Extract the indices of the strings to be concatenated
        a, b = map(int, operation.split())

        # Concatenate the strings and store the result in the dictionary
        concatenated_strings[a] = concatenated_strings.get(a, "") + strings[b]

        # Make the second string empty
        strings[b] = ""

    # Return the last string that remains
    return concatenated_strings[1]

