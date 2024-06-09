
def solve(s, t):
    # Initialize variables
    max_occurrences = 0
    occurrences = 0
    i = 0

    # Loop through the string s and check if the substring t can be found
    while i < len(s):
        # If the substring t is found, replace it with the corresponding letter from string t and increment the number of occurrences
        if s[i:i+len(t)] == t:
            s = s[:i] + t[0] + s[i+len(t):]
            occurrences += 1
        i += 1

    # Return the maximum number of occurrences
    return occurrences

