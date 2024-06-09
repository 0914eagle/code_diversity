
def get_min_changes(s, k):
    # Initialize variables
    n = len(s)
    count_r = s.count("R")
    count_g = s.count("G")
    count_b = s.count("B")
    min_changes = n
    
    # Loop through all possible combinations of R, G, and B
    for i in range(0, n + 1):
        for j in range(0, n + 1 - i):
            for k in range(0, n + 1 - i - j):
                # Check if the current combination is valid
                if i + j + k == n:
                    # Calculate the number of changes needed
                    changes = abs(count_r - i) + abs(count_g - j) + abs(count_b - k)
                    # Update the minimum number of changes if needed
                    if changes < min_changes:
                        min_changes = changes
    
    # Return the minimum number of changes
    return min_changes

