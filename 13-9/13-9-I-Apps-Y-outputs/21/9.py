
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of changes needed
    min_changes = len(s)
    
    # Loop through each possible starting index in S
    for i in range(len(s) - len(t) + 1):
        # Check if T is a substring of S starting at index i
        if s[i:i+len(t)] == t:
            # If T is a substring, update the minimum number of changes needed
            min_changes = min(min_changes, len(s) - len(t) - i + 1)
    
    # Return the minimum number of changes needed
    return min_changes

