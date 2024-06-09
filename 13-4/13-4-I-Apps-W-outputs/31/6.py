
def solve(r, b, k):
    # Calculate the maximum number of planks that can be painted
    max_planks = 10**100
    
    # Initialize a list to store the painted planks
    painted_planks = []
    
    # Iterate through the planks and paint them according to the rules
    for i in range(max_planks):
        # If the index of the plank is divisible by r, paint it red
        if i % r == 0:
            painted_planks.append("R")
        # If the index of the plank is divisible by b, paint it blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the index of the plank is divisible by both r and b, choose the color to paint it
        elif i % (r*b) == 0:
            painted_planks.append("R")
        # Otherwise, don't paint the plank
        else:
            continue
    
    # Check if there are k consecutive planks with the same color in the painted planks list
    for i in range(len(painted_planks) - k + 1):
        if len(set(painted_planks[i:i+k])) == 1:
            return "REBEL"
    
    # If no consecutive planks with the same color are found, return "OBEY"
    return "OBEY"

