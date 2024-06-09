
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of changes needed
    min_changes = len(s)
    # Loop through each possible starting index in S
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of S starting at index i is equal to T
        if s[i:i+len(t)] == t:
            # If it is, return the minimum number of changes needed (0)
            return 0
        # If it's not, check if the number of changes needed is less than the current minimum
        if len(s) - len(t) - i < min_changes:
            # If it is, update the minimum number of changes needed
            min_changes = len(s) - len(t) - i
    # Return the minimum number of changes needed
    return min_changes

