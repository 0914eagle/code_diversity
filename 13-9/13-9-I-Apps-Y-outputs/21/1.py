
def solve(s, t):
    # Initialize a variable to store the minimum number of changes needed
    min_changes = len(s)
    # Loop through each possible starting index in S
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of S starting at index i is equal to T
        if s[i:i+len(t)] == t:
            # If it is, update the minimum number of changes needed
            min_changes = min(min_changes, len(s) - i - len(t) + 1)
    # Return the minimum number of changes needed
    return min_changes

