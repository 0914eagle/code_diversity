
def solve(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Loop through all the planks
    for i in range(10**100):
        # Check if the current plank is divisible by r and b
        if i % r == 0 and i % b == 0:
            # If both conditions are true, choose a color randomly
            if random.randint(0, 1) == 0:
                painted_planks.append("R")
            else:
                painted_planks.append("B")
        elif i % r == 0:
            # If the current plank is divisible by r, paint it red
            painted_planks.append("R")
        elif i % b == 0:
            # If the current plank is divisible by b, paint it blue
            painted_planks.append("B")

    # Check if there are any consecutive planks with the same color
    for i in range(len(painted_planks) - k + 1):
        if len(set(painted_planks[i:i+k])) == 1:
            # If there are consecutive planks with the same color, return REBEL
            return "REBEL"

    # If no consecutive planks with the same color are found, return OBEY
    return "OBEY"

