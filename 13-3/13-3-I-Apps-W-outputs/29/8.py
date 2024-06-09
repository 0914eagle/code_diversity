
def solve(n, positions):
    # Sort the positions in ascending order
    positions.sort()

    # Initialize the minimum time to collect all prizes
    time = 0

    # Iterate through the positions and calculate the time to collect each prize
    for i in range(n - 1):
        time += abs(positions[i] - positions[i + 1])

    return time

