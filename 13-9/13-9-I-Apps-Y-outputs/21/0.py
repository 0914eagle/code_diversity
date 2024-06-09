
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of characters to be changed
    min_changes = len(s)
    # Loop through each position in S
    for i in range(len(s)):
        # Check if the current position in S is a prefix of T
        if s[i:i+len(t)] == t:
            # If it is, calculate the number of characters that need to be changed
            changes = len(s) - len(t)
            # Update the minimum number of characters to be changed if necessary
            min_changes = min(min_changes, changes)
    # Return the minimum number of characters to be changed
    return min_changes

