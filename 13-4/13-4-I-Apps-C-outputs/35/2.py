
def solve(s):
    # Initialize a dictionary to store the count of hidden strings
    hidden_strings = {}

    # Loop through each substring of the text
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            # Check if the substring is a hidden string
            if is_hidden_string(s[i:j+1]):
                # If it is, increment the count in the dictionary
                if s[i:j+1] in hidden_strings:
                    hidden_strings[s[i:j+1]] += 1
                else:
                    hidden_strings[s[i:j+1]] = 1

    # Return the maximum count
    return max(hidden_strings.values())

# Check if a substring is a hidden string
def is_hidden_string(s):
    # Check if the substring is a subsequence of the text
    if s in s:
        # Check if the indices form an arithmetic progression
        indices = [i for i, ltr in enumerate(s) if ltr in s]
        if len(indices) > 2 and indices[1] - indices[0] == indices[2] - indices[1]:
            return True

    return False

