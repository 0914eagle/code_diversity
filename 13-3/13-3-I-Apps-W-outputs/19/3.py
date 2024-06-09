
def solve(n, k, arrangement):
    # Initialize a list to store the pairs of children who will turn left
    pairs_left = []
    
    # Iterate through each move
    for move in range(k):
        # Initialize a list to store the pairs of children who will turn right
        pairs_right = []
        
        # Iterate through each pair of children
        for i in range(n-1):
            # If the current child and the next child are looking at each other
            if arrangement[i] == arrangement[i+1]:
                # Add the pair to the list of pairs who will turn left
                pairs_left.append((i, i+1))
            # If the current child and the next child are not looking at each other
            else:
                # Add the pair to the list of pairs who will turn right
                pairs_right.append((i, i+1))
        
        # If there are no pairs who will turn left, return -1
        if not pairs_left:
            return -1
        
        # Iterate through each pair who will turn left
        for pair in pairs_left:
            # If the current child is looking to the left
            if arrangement[pair[0]] == "L":
                # Turn the child to the right
                arrangement[pair[0]] = "R"
            # If the current child is looking to the right
            else:
                # Turn the child to the left
                arrangement[pair[0]] = "L"
        
        # Iterate through each pair who will turn right
        for pair in pairs_right:
            # If the current child is looking to the left
            if arrangement[pair[0]] == "L":
                # Turn the child to the left
                arrangement[pair[0]] = "L"
            # If the current child is looking to the right
            else:
                # Turn the child to the right
                arrangement[pair[0]] = "R"
        
        # Print the number of pairs who will turn left and their positions
        print(len(pairs_left), *[pair[0] for pair in pairs_left])
    
    # Return the final arrangement
    return "".join(arrangement)

