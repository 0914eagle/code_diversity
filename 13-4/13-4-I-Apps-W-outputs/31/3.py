
def solve(r, b, k):
    # Calculate the maximum number of planks that can be painted
    max_planks = 10**100
    
    # Initialize a list to store the painted planks
    painted_planks = []
    
    # Iterate through the planks and paint them according to the rules
    for i in range(max_planks):
        # Check if the current plank is divisible by r
        if i % r == 0:
            # Paint the current plank red
            painted_planks.append("R")
        # Check if the current plank is divisible by b
        elif i % b == 0:
            # Paint the current plank blue
            painted_planks.append("B")
        # Check if the current plank is divisible by both r and b
        elif i % r == 0 and i % b == 0:
            # Paint the current plank according to the Government's rule
            if len(painted_planks) == 0 or painted_planks[-1] != "R":
                painted_planks.append("R")
            else:
                painted_planks.append("B")
    
    # Check if there are k consecutive planks with the same color in the painted_planks list
    for i in range(len(painted_planks) - k + 1):
        if len(set(painted_planks[i:i+k])) == 1:
            return "REBEL"
    
    return "OBEY"

