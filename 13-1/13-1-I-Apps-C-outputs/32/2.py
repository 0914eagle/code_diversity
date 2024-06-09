
def solve(n, a):
    # Initialize a 2D array to store the configuration of targets
    targets = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize a variable to store the number of targets
    num_targets = 0

    # Loop through each column
    for i in range(1, n + 1):
        # Get the number of targets for this column
        num_hits = a[i - 1]

        # Loop through each row
        for j in range(1, n + 1):
            # If the target is not already placed and there is still space in this row
            if targets[j][i] == 0 and targets[j][0] < 2:
                # Place the target and increment the number of targets
                targets[j][i] = 1
                num_targets += 1

                # If the target has hit the maximum number of targets, break
                if num_targets == num_hits:
                    break

        # If the target has not hit the maximum number of targets, return -1
        if num_targets < num_hits:
            return -1

    # Return the configuration of targets
    return targets

