
def get_min_changes(s, k):
    # Initialize variables
    n = len(s)
    changes = 0
    i = 0
    j = 0
    
    # Loop through the string
    while i < n and j < k:
        # If the current character is not 'R', 'G', or 'B', change it to 'R'
        if s[i] not in ["R", "G", "B"]:
            changes += 1
            s = s[:i] + "R" + s[i+1:]
            n += 1
        
        # If the current character is 'R', 'G', or 'B', increment j
        elif s[i] in ["R", "G", "B"]:
            j += 1
        
        # Increment i
        i += 1
    
    # Return the minimum number of changes needed
    return changes

