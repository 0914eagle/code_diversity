
def solve(strings):
    # Initialize a dictionary to store the longest subsequence for each string
    longest_subsequence = {}

    # Iterate over the strings
    for string in strings:
        # Initialize the longest subsequence for the current string as an empty string
        longest_subsequence[string] = ""

        # Iterate over the characters in the current string
        for i in range(len(string)):
            # Check if the current character is the same as the first character of the longest subsequence
            if string[i] == longest_subsequence[string][0]:
                # If it is, update the longest subsequence to include the current character
                longest_subsequence[string] += string[i]

    # Initialize a set to store the unique substrings
    unique_substrings = set()

    # Iterate over the strings
    for string in strings:
        # Add the longest subsequence for the current string to the set of unique substrings
        unique_substrings.add(longest_subsequence[string])

    # Return the length of the set of unique substrings
    return len(unique_substrings)

