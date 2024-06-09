
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of changes needed
    min_changes = len(s)
    
    # Loop through each substring of S that is the same length as T
    for i in range(len(s) - len(t) + 1):
        # Check if the substring is equal to T
        if s[i:i+len(t)] == t:
            # If it is, return the minimum number of changes needed (0)
            return 0
    
    # If we reach this point, T is not a substring of S
    # Return the minimum number of changes needed (the length of S)
    return min_changes

