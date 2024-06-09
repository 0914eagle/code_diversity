
def solve(n, k, arr):
    # Initialize a list to store the pairs of children who turn left
    pairs = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and the current move is even
        if arr[i] != arr[i+1] and k % 2 == 0:
            # Add the pair to the list of pairs who turn left
            pairs.append((i+1, i+2))
    
    # If there are no pairs who turn left, return -1
    if not pairs:
        return -1
    
    # Initialize a list to store the numbers of the children who turn left
    children = []
    
    # Loop through each pair who turn left
    for pair in pairs:
        # Add the first child in the pair to the list of children who turn left
        children.append(pair[0])
        # Add the second child in the pair to the list of children who turn left
        children.append(pair[1])
    
    # Return the list of children who turn left
    return children

