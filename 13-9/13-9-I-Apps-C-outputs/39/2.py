
def solve(n, a):
    # Initialize a 2D array to store the number of targets in each row and column
    targets = [[0] * (n + 1) for _ in range(n + 1)]

    # Populate the array with the given number of targets for each column
    for i in range(n):
        targets[0][i + 1] = a[i]

    # Iterate through each row and column
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the target is already placed in this row or column, skip it
            if targets[i][0] > 0 or targets[0][j] > 0:
                continue

            # If the target is not placed and the number of targets in this row and column is less than 2, place the target
            if targets[i][j] == 0 and targets[i][0] + targets[0][j] < 2:
                targets[i][j] = 1
                targets[i][0] += 1
                targets[0][j] += 1

    # Check if all targets have been placed
    if all(targets[i][0] == a[i - 1] for i in range(1, n + 1)):
        # If all targets have been placed, return the configuration
        return targets[1:]

    # If not all targets have been placed, return -1
    return -1

