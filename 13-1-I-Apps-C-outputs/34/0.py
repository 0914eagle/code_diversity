
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
    
    # If the length of the swaps list is equal to the number of pairs of positions,
    # it is possible to swap all pairs of positions so that the permutation stays the same
    if len(swaps) == n * (n - 1) // 2:
        return "YES"
    else:
        return "NO"

