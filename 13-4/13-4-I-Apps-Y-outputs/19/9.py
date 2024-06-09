
def solve(n, remembered_kids):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered_dict = {}
    for i in range(n):
        remembered_dict[i+1] = set(remembered_kids[i])
    
    # Initialize a set to keep track of the kids that have been placed in the circle
    placed_kids = set()
    
    # Initialize the permutation of kids
    permutation = [0] * n
    
    # Start placing kids in the circle
    current_kid = 1
    while len(placed_kids) < n:
        # Get the remembered kids for the current kid
        remembered_kids = remembered_dict[current_kid]
        
        # Find the next kid to place in the circle
        next_kid = 1
        while next_kid in placed_kids or next_kid not in remembered_kids:
            next_kid += 1
        
        # Place the next kid in the circle
        permutation[current_kid-1] = next_kid
        placed_kids.add(next_kid)
        
        # Update the remembered kids for the current kid
        remembered_dict[current_kid] = remembered_dict[current_kid] - {next_kid}
        
        # Move on to the next kid
        current_kid = next_kid
    
    return permutation

