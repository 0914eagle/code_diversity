
def solve(n):
    # If n is odd, it is not possible to swap all pairs of positions so that the permutation stays the same
    if n % 2 == 1:
        return "NO"
    
    # Initialize the permutation as [1, 2, 3, ..., n]
    permutation = list(range(1, n + 1))
    
    # Initialize the number of swaps to be performed
    num_swaps = n * (n - 1) // 2
    
    # Initialize the list of swaps to be performed
    swaps = []
    
    # Loop through each pair of positions (i, j), where i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            # If the positions are not already swapped
            if permutation[i] != i + 1 or permutation[j] != j + 1:
                # Perform the swap
                permutation[i], permutation[j] = permutation[j], permutation[i]
                # Add the swap to the list of swaps
                swaps.append((i + 1, j + 1))
                # Decrement the number of swaps to be performed
                num_swaps -= 1
    
    # If all pairs of positions have been swapped
    if num_swaps == 0:
        return "YES\n" + "\n".join([f"{a} {b}" for a, b in swaps])
    else:
        return "NO"

