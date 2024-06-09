
def solve(N, strings):
    # Initialize a dictionary to store the longest subsequence for each string
    longest_subsequence = {}

    # Iterate over each string
    for string in strings:
        # Initialize the longest subsequence for the current string as an empty list
        longest_subsequence[string] = []

        # Iterate over each character in the string
        for i in range(len(string)):
            # If the character is already in the longest subsequence, skip it
            if string[i] in longest_subsequence[string]:
                continue

            # If the character is not in the longest subsequence, find the longest subsequence that starts with it
            longest_substring = string[i:]
            for j in range(i + 1, len(string)):
                if string[j] == string[i]:
                    longest_substring += string[j]

            # Update the longest subsequence for the current string
            longest_subsequence[string] = longest_substring

    # Find the longest subsequence that is common to all strings
    common_subsequence = []
    for string in strings:
        for char in longest_subsequence[string]:
            if char not in common_subsequence:
                common_subsequence.append(char)

    # Return the length of the common subsequence
    return len(common_subsequence)

