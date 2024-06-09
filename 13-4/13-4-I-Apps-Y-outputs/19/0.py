
def solve(n, remembered_pairs):
    # Initialize a dictionary to map each kid to its remembered pairs
    remembered_dict = {}
    for i in range(n):
        remembered_dict[i+1] = set(remembered_pairs[i])
    
    # Initialize a set to store the remaining kids
    remaining_kids = set(range(1, n+1))
    
    # Initialize the permutation of kids
    permutation = []
    
    # Start from the first kid and iterate through the kids
    current_kid = 1
    while remaining_kids:
        # Get the remembered pairs for the current kid
        remembered_pairs = remembered_dict[current_kid]
        
        # If the current kid has no remembered pairs, it means it is the last kid in the circle
        if not remembered_pairs:
            permutation.append(current_kid)
            break
        
        # If the current kid has only one remembered pair, it means it is the first kid in the circle
        if len(remembered_pairs) == 1:
            permutation.append(current_kid)
            current_kid = list(remembered_pairs)[0]
            continue
        
        # If the current kid has two remembered pairs, it means it is in the middle of the circle
        if len(remembered_pairs) == 2:
            # Get the next kid for the current kid
            next_kid = list(remembered_pairs - {current_kid})[0]
            
            # Add the current kid to the permutation
            permutation.append(current_kid)
            
            # Set the current kid as the next kid
            current_kid = next_kid
            continue
    
    # Return the permutation of kids
    return permutation

