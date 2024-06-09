
def solve(n, a):
    # Initialize a 2D array to store the configuration of targets
    targets = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize a variable to store the number of targets
    num_targets = 0

    # Loop through each column
    for i in range(1, n + 1):
        # Get the number of hits for the current column
        hits = a[i - 1]

        # Loop through each row in the column
        for j in range(1, n + 1):
            # If the current cell is not already occupied by a target
            if targets[j][i] == 0:
                # Place a target in the current cell
                targets[j][i] = 1
                num_targets += 1

                # If the number of hits is greater than 0, place another target in the cell below the current cell
                if hits > 0:
                    targets[j + 1][i] = 1
                    num_targets += 1
                    hits -= 1

    # If the number of targets is not equal to the total number of hits, return -1
    if num_targets != sum(a):
        return -1

    # Otherwise, return the configuration of targets
    return targets

