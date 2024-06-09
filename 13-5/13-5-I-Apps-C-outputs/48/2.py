
def solve(N, strings):
    # Initialize a dictionary to store the longest subsequence for each string
    longest_subsequence = {}

    # Iterate over each string
    for string in strings:
        # Initialize the longest subsequence for the current string as an empty list
        longest_subsequence[string] = []

        # Iterate over each character in the string
        for i in range(len(string)):
            # If the current character is not already in the longest subsequence, add it
            if string[i] not in longest_subsequence[string]:
                longest_subsequence[string].append(string[i])

            # If the current character is already in the longest subsequence, check if it is the start and end of a subsequence
            else:
                # Get the index of the current character in the longest subsequence
                index = longest_subsequence[string].index(string[i])

                # If the current character is the start and end of a subsequence, add it to the longest subsequence
                if index == 0 or index == len(longest_subsequence[string]) - 1:
                    longest_subsequence[string].append(string[i])

    # Initialize a set to store the unique substrings
    unique_substrings = set()

    # Iterate over each string
    for string in strings:
        # Iterate over each character in the longest subsequence of the current string
        for substring in longest_subsequence[string]:
            # If the substring is not already in the set of unique substrings, add it
            if substring not in unique_substrings:
                unique_substrings.add(substring)

    # Return the length of the set of unique substrings
    return len(unique_substrings)

