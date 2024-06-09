
def is_possible_to_swap_all_pairs(permutation):
    n = len(permutation)
    # Check if the permutation is already in the desired form
    if permutation == list(range(1, n + 1)):
        return "YES"
    
    # Initialize a set to keep track of the positions that have been swapped
    swapped_positions = set()
    
    # Iterate through each pair of positions
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Check if the positions have already been swapped
            if (i, j) in swapped_positions or (j, i) in swapped_positions:
                continue
            
            # Swap the positions and check if the permutation is now in the desired form
            permutation[i], permutation[j] = permutation[j], permutation[i]
            if permutation == list(range(1, n + 1)):
                return "YES"
            
            # Undo the swap and mark the positions as swapped
            permutation[i], permutation[j] = permutation[j], permutation[i]
            swapped_positions.add((i, j))
    
    # If we reach this point, it means that it is not possible to swap all pairs of positions so that the permutation stays the same
    return "NO"

