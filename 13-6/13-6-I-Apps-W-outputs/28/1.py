
def solve(s, t):
    # Replace all '?' characters with all lowercase letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize a counter for the number of non-intersecting occurrences of t
    count = 0
    # Iterate over all possible pairs of positions in s
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of s starting at position i and ending at position i + len(t) - 1 is equal to t
        if s[i:i+len(t)] == t:
            # Increment the counter
            count += 1
    # Return the string s with the maximum number of non-intersecting occurrences of t
    return s

