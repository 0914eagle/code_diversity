
def count_occurrences(s):
    # Initialize a dictionary to store the count of each hidden string
    hidden_strings = {}

    # Loop through each substring of the text
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Check if the substring is a hidden string
            substring = s[i:j]
            if substring not in hidden_strings:
                hidden_strings[substring] = 1
            else:
                hidden_strings[substring] += 1

    # Return the maximum count
    return max(hidden_strings.values())

