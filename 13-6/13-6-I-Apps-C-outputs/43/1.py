
def count_occurrences(s):
    # Initialize a dictionary to store the count of each hidden string
    hidden_strings = {}

    # Loop through each substring of the text
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Check if the substring is a hidden string
            if s[i:j] in hidden_strings:
                # If it is, increment the count
                hidden_strings[s[i:j]] += 1
            else:
                # If it's not, add it to the dictionary with count 1
                hidden_strings[s[i:j]] = 1

    # Return the maximum count
    return max(hidden_strings.values())

