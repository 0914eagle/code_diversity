
def solve(n, k, arr):
    # Initialize a list to store the pairs of children who turn left
    pairs = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it's the first move, add them to the list of pairs
        if arr[i] != arr[i+1] and len(pairs) == 0:
            pairs.append([i, i+1])
    
    # Loop through each move
    for move in range(k-1):
        # If there are no pairs left, return -1
        if not pairs:
            return -1
        
        # Initialize a list to store the children who turn left in this move
        turn_left = []
        
        # Loop through each pair
        for pair in pairs:
            # If the children are looking at each other, add them to the list of children who turn left
            if arr[pair[0]] == arr[pair[1]]:
                turn_left.append(pair[0])
                turn_left.append(pair[1])
        
        # Remove the pairs from the list of pairs
        pairs = [pair for pair in pairs if pair not in turn_left]
        
        # Add the children who turn left to the list of children who turn left in this move
        turn_left = list(set(turn_left))
        
        # Print the number of children who turn left and their positions
        print(len(turn_left))
        print(" ".join(map(str, turn_left)))
        
    # If there are still pairs left, return -1
    if pairs:
        return -1
    
    # If the process is finished, return 1
    return 1

