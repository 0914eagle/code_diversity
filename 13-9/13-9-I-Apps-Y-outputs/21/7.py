
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of changes needed
    min_changes = len(s)
    
    # Iterate through all possible starting indices in S
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of S starting at index i matches T
        if s[i:i+len(t)] == t:
            # If it matches, we don't need to make any changes
            return 0
        # If it doesn't match, we need to change at least one character
        min_changes = min(min_changes, len(s) - i - len(t) + 1)
    
    # Return the minimum number of changes needed
    return min_changes

