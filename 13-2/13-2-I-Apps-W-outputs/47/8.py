
def solve(n, m, k, arrays):
    # Initialize the array of pairs
    pairs = []

    # Loop through each array
    for i in range(n):
        # Find the indices of the smallest and largest elements
        smallest = arrays[i].index(min(arrays[i])) + 1
        largest = arrays[i].index(max(arrays[i])) + 1

        # If the arrays are not already sorted, add the pair of indices to the array
        if (k == 0 and arrays[i][smallest] > arrays[i][largest]) or (k == 1 and arrays[i][smallest] < arrays[i][largest]):
            pairs.append([smallest, largest])

    # Return the array of pairs
    return pairs

