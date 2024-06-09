
def solve(r, b, k):
    # Calculate the maximum number of planks that can be painted
    max_planks = 10**100
    
    # Initialize a list to store the painted planks
    painted_planks = []
    
    # Iterate through the planks and paint them according to the given conditions
    for i in range(max_planks):
        # If the index of the plank is divisible by r, paint it red
        if i % r == 0:
            painted_planks.append("R")
        # If the index of the plank is divisible by b, paint it blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the index of the plank is divisible by both r and b, paint it according to the given conditions
        elif i % r == 0 and i % b == 0:
            if len(painted_planks) == 0 or painted_planks[-1] != "R":
                painted_planks.append("R")
            else:
                painted_planks.append("B")
        # If the index of the plank is not divisible by r, b, or both, do not paint it
        else:
            continue
    
    # Check if there are k consecutive planks with the same color in the painted planks list
    for i in range(len(painted_planks) - k + 1):
        if len(set(painted_planks[i:i+k])) == 1:
            return "REBEL"
    
    # If there are no consecutive planks with the same color, return "OBEY"
    return "OBEY"

