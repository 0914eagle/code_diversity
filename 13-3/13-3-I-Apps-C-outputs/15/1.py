
def solve(walk):
    # Initialize a dictionary to store the values of the walks
    values = {}
    
    # Initialize the root node with value 1
    values[1] = 1
    
    # Iterate through the walk string
    for char in walk:
        # If the current character is 'L', 'R' or 'P', update the value of the current node
        if char in 'LRP':
            values[values[1]] = 2 * values[1] if char == 'L' else 2 * values[1] + 1
        # If the current character is '*', update the value of the current node and its children
        elif char == '*':
            values[values[1]] = values[2 * values[1]] + values[2 * values[1] + 1]
    
    # Return the value of the walk
    return values[1]

