
def solve(n, k, arrangement):
    # Initialize a list to store the pairs of children who will turn left
    pairs_to_turn_left = []
    
    # Loop through each pair of children and check if they are looking at each other
    for i in range(n-1):
        if arrangement[i] == arrangement[i+1]:
            # If they are looking at each other, add them to the list of pairs to turn left
            pairs_to_turn_left.append((i, i+1))
    
    # If there are no pairs to turn left, return -1
    if not pairs_to_turn_left:
        return -1
    
    # Initialize a list to store the numbers of the children who will turn left
    children_to_turn_left = []
    
    # Loop through each pair of children who will turn left and add their numbers to the list
    for pair in pairs_to_turn_left:
        children_to_turn_left.extend(pair)
    
    # Return the list of children who will turn left
    return children_to_turn_left

