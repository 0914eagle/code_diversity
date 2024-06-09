
def solve(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Loop through each plank and paint it according to the conditions
    for i in range(10**100):
        # If the index is divisible by r, paint it red
        if i % r == 0:
            painted_planks.append("R")
        # If the index is divisible by b, paint it blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the index is divisible by both r and b, choose the color to paint it
        elif i % r == 0 and i % b == 0:
            painted_planks.append("R")
        # Otherwise, don't paint the plank
        else:
            continue

    # Check if there are any consecutive planks with the same color
    for i in range(len(painted_planks) - 1):
        if painted_planks[i] == painted_planks[i + 1]:
            # If there are k consecutive planks with the same color, return "REBEL"
            if i + k < len(painted_planks):
                return "REBEL"

    # If there are no consecutive planks with the same color, return "OBEY"
    return "OBEY"

