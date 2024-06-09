
def solve(walk):
    # Initialize a dictionary to store the values of each walk
    values = {}

    # Initialize the root node with value 1
    values[""] = 1

    # Iterate through the walk string
    for move in walk:
        # If the move is 'L', update the values of the left child
        if move == "L":
            for key in values:
                values[key + "L"] = values[key] * 2
        # If the move is 'R', update the values of the right child
        elif move == "R":
            for key in values:
                values[key + "R"] = values[key] * 2 + 1
        # If the move is 'P', update the values of the current node
        elif move == "P":
            for key in values:
                values[key + "P"] = values[key]
        # If the move is '*', update the values of all possible walks
        elif move == "*":
            for key in values:
                values[key + "L"] = values[key] * 2
                values[key + "R"] = values[key] * 2 + 1
                values[key + "P"] = values[key]

    # Return the sum of all values in the dictionary
    return sum(values.values())

