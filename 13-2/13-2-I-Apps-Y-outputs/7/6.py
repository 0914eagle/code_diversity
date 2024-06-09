
def solve(s, t):
    # Initialize the result string
    result = "UNRESTORABLE"

    # Iterate through all possible strings that satisfy Condition 1
    for i in range(26):
        # Create a new string by replacing the ? with the ith letter of the alphabet
        new_string = s.replace("?", chr(i + 97))

        # Check if the new string contains T as a contiguous substring
        if t in new_string:
            # If it does, check if it is lexicographically smaller than the current result
            if new_string < result:
                # If it is, update the result
                result = new_string

    # Return the result
    return result

