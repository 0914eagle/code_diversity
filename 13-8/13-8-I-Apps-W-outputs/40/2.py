
def get_max_occurrences(s, t):
    # Initialize a dictionary to store the count of each substring
    # of length |t| in s
    substring_counts = {}

    # Loop through each substring of length |t| in s
    for i in range(len(s) - len(t) + 1):
        substring = s[i:i+len(t)]

        # If the substring is already in the dictionary, increment its count
        if substring in substring_counts:
            substring_counts[substring] += 1

        # Otherwise, add the substring to the dictionary with count 1
        else:
            substring_counts[substring] = 1

    # Return the maximum count of any substring in the dictionary
    return max(substring_counts.values())

