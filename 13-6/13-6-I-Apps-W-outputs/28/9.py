
def solve(s, t):
    # Replace all '?' characters with all possible lowercase letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize a counter to keep track of the maximum suitability
    max_suitability = 0
    # Initialize a variable to store the string with the maximum suitability
    max_string = ""
    # Iterate over all possible strings
    for i in range(len(s) - len(t) + 1):
        # Extract a substring of length len(t) starting from index i
        substring = s[i:i+len(t)]
        # Check if the substring is equal to t
        if substring == t:
            # If it is, increment the counter
            max_suitability += 1
            # And update the string with the maximum suitability
            max_string = s
    # Return the string with the maximum suitability
    return max_string

