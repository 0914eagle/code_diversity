
def solve(s, t):
    # Initialize a variable to store the minimum number of changes
    min_changes = len(s)
    # Loop through each position in S
    for i in range(len(s)):
        # Check if the substring of S starting from the current position is equal to T
        if s[i:i+len(t)] == t:
            # If it is, calculate the number of changes needed by comparing the lengths of S and T
            min_changes = min(min_changes, len(s) - len(t))
    # Return the minimum number of changes
    return min_changes

