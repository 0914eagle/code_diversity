
def solve(s, t):
    # Initialize a variable to keep track of the minimum number of changes needed
    min_changes = len(s)
    
    # Loop through each possible starting index in S
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of S starting at index i matches T
        if s[i:i+len(t)] == t:
            # If it matches, we need to change no characters
            min_changes = 0
            break
        # If it doesn't match, we need to change at least one character
        else:
            min_changes = 1
    
    return min_changes

