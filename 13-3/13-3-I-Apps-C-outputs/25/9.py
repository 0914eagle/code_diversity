
def solve(n):
    if n == 1:
        return "YES"
    
    # Initialize a list to store the positions of the swaps
    swaps = []
    
    # Iterate through each pair of positions (i, j) where i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            # If the positions are not already swapped, swap them
            if i != j:
                swaps.append([i, j])
    
    # If the number of swaps is equal to the number of positions, return "YES"
    if len(swaps) == n:
        return "YES"
    else:
        return "NO"

