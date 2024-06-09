
def solve(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    positions.sort(key=lambda x: x[0])

    # Initialize the positions of you and your coworker
    you = [0, 0]
    coworker = [0, 0]

    # Divide the swimmers into two groups
    group_1 = positions[:n//2]
    group_2 = positions[n//2:]

    # Find the midpoint between the two groups
    midpoint = (sum(x[0] for x in group_1) + sum(x[0] for x in group_2)) / (n)

    # Move you and your coworker to the midpoint
    you[0] = midpoint
    coworker[0] = midpoint

    # Move you and your coworker to the same y-coordinate as the closest swimmer
    you[1] = min(positions, key=lambda x: abs(x[1] - midpoint))[1]
    coworker[1] = you[1]

    return you, coworker

