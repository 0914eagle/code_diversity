
def solve(n):
    # Base case: if n is 1, there is only one permutation, so return "YES"
    if n == 1:
        return "YES"
    
    # Initialize a list to store the positions of the swaps
    swaps = []
    
    # Loop through each pair of positions (i, j), where i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            # If the positions are not already swapped, swap them
            if i != j:
                swaps.append([i, j])
    
    # If the length of the swaps list is n - 1, it means that all pairs of positions have been swapped, so return "YES"
    if len(swaps) == n - 1:
        return "YES"
    else:
        return "NO"

