
def solve(s, t):
    # Initialize a variable to store the minimum number of changes needed
    min_changes = len(s)
    # Loop through each position in S
    for i in range(len(s)):
        # Check if the substring of S starting from position i is equal to T
        if s[i:i+len(t)] == t:
            # If it is, update the minimum number of changes needed
            min_changes = min(min_changes, len(s) - i)
    # Return the minimum number of changes needed
    return min_changes

