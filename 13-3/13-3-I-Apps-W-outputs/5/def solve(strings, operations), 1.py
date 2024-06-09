
def solve(strings, operations):
    # Initialize an empty dictionary to store the concatenated strings
    concatenated_strings = {}

    # Loop through each operation
    for operation in operations:
        # Split the operation into the indices of the strings to concatenate
        a, b = map(int, operation.split())

        # Concatenate the strings and store the result in the dictionary
        concatenated_strings[a] = concatenated_strings.get(a, "") + strings[b]

        # Empty the string at index b
        strings[b] = ""

    # Return the last string that remains
    return concatenated_strings[len(concatenated_strings)]

