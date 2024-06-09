
def solve(s, t):
    # Initialize variables
    max_occurrences = 0
    occurrences = 0
    i = 0

    # Loop through the string s and replace the question marks with letters from t
    while i < len(s):
        if s[i] == "?":
            s = s[:i] + t[occurrences % len(t)] + s[i+1:]
            occurrences += 1
        i += 1

    # Return the maximum number of occurrences of string t
    return occurrences

