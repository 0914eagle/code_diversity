
def solve(walk):
    # Initialize a dictionary to store the values of the walks
    values = {}
    
    # Initialize the root node with value 1
    values[""] = 1
    
    # Iterate through the walk string
    for move in walk:
        # If the move is 'L', add the left child to the dictionary
        if move == 'L':
            for key in values.keys():
                values[key + "L"] = values[key] * 2
        # If the move is 'R', add the right child to the dictionary
        elif move == 'R':
            for key in values.keys():
                values[key + "R"] = values[key] * 2 + 1
        # If the move is 'P', stay in the same node
        elif move == 'P':
            for key in values.keys():
                values[key + "P"] = values[key]
        # If the move is '*', add all possible moves to the dictionary
        elif move == '*':
            for key in values.keys():
                values[key + "L"] = values[key] * 2
                values[key + "R"] = values[key] * 2 + 1
                values[key + "P"] = values[key]
    
    # Return the sum of all values in the dictionary
    return sum(values.values())

