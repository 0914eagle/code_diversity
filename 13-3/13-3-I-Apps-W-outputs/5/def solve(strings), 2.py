
def solve(strings):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the strings and operations
    for string, operation in zip(strings, operations):
        # If the operation is to concatenate two strings, concatenate them and store the result in the first string
        if operation[0] != operation[1]:
            strings[operation[0] - 1] += strings[operation[1] - 1]
        # If the operation is to make a string empty, set the string to an empty string
        else:
            strings[operation[0] - 1] = ""

    # Return the last string that remains
    return strings[-1]

