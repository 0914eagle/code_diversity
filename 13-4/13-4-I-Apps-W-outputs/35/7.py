
def find_min_swaps(permutation):
    n = len(permutation)
    # Initialize a dictionary to store the number of swaps for each pair of indices
    swaps = {}
    # Loop through each pair of indices
    for i in range(n):
        for j in range(i+1, n):
            # If the elements are not in order, add the pair to the dictionary with the number of swaps as the value
            if permutation[i] > permutation[j]:
                swaps[(i, j)] = 1
            # If the elements are in order, add the pair to the dictionary with 0 as the value
            else:
                swaps[(i, j)] = 0
    
    # Find the minimum number of swaps and the corresponding pairs
    min_swaps = float('inf')
    min_pairs = []
    for pair, swaps in swaps.items():
        if swaps < min_swaps:
            min_swaps = swaps
            min_pairs = [pair]
        elif swaps == min_swaps:
            min_pairs.append(pair)
    
    return min_swaps, len(min_pairs)

