
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
    
    # If all pairs of positions are swapped, return "YES" and the list of swaps
    if len(swaps) == n * (n - 1) // 2:
        return "YES\n" + "\n".join([str(swap[0]) + " " + str(swap[1]) for swap in swaps])
    
    # Otherwise, return "NO"
    return "NO"

