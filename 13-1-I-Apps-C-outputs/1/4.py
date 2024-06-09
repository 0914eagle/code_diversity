
def solve(N, strings):
    # Initialize a dictionary to store the longest subsequence for each string
    longest_subsequence = {}

    # Iterate over each string
    for string in strings:
        # Initialize the longest subsequence for the current string as an empty list
        longest_subsequence[string] = []

        # Iterate over each character in the string
        for i in range(len(string)):
            # If the character is not already in the longest subsequence, add it
            if string[i] not in longest_subsequence[string]:
                longest_subsequence[string].append(string[i])

            # If the character is already in the longest subsequence, check if it is a match
            else:
                # Get the index of the character in the longest subsequence
                index = longest_subsequence[string].index(string[i])

                # If the character is a match, update the longest subsequence
                if string.startswith(string[i]) and string.endswith(string[i]):
                    longest_subsequence[string] = longest_subsequence[string][:index + 1]

    # Return the length of the longest subsequence for all strings
    return len(max(longest_subsequence.values(), key=len))

