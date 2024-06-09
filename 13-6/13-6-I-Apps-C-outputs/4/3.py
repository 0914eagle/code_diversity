
def solve(n):
    # Check if n is valid
    if n < 1 or n > 1000:
        return "NO"
    
    # Initialize the permutation as a list of numbers from 1 to n
    permutation = list(range(1, n + 1))
    
    # Initialize the number of swaps to be performed
    num_swaps = n * (n - 1) // 2
    
    # Initialize the list of swaps to be performed
    swaps = []
    
    # Loop through each pair of positions
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Check if the swap is valid
            if permutation[i] != permutation[j]:
                # Add the swap to the list of swaps
                swaps.append((i, j))
                # Perform the swap
                permutation[i], permutation[j] = permutation[j], permutation[i]
                # Decrement the number of swaps to be performed
                num_swaps -= 1
    
    # Check if all swaps have been performed
    if num_swaps == 0:
        return "YES"
    else:
        return "NO"

