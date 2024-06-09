
def solve(N, strings):
    # Initialize a dictionary to store the longest subsequence for each string
    longest_subsequence = {}

    # Iterate over each string
    for string in strings:
        # Initialize the longest subsequence for the current string to 1
        longest_subsequence[string] = 1

        # Iterate over the remaining strings
        for other_string in strings:
            # If the current string is a prefix of the other string and a suffix of the other string
            if string in other_string and other_string.endswith(string):
                # Update the longest subsequence for the current string if necessary
                longest_subsequence[string] = max(longest_subsequence[string], longest_subsequence[other_string] + 1)

    # Return the maximum longest subsequence over all strings
    return max(longest_subsequence.values())

