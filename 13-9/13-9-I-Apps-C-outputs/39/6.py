
def get_target_config(hits):
    # Initialize a dictionary to store the number of targets for each row and column
    targets = {}
    for i in range(1, len(hits) + 1):
        targets[i] = {}
        for j in range(1, len(hits) + 1):
            targets[i][j] = 0

    # Populate the dictionary with the given number of hits for each column
    for i, hits_per_column in enumerate(hits):
        targets[1][i + 1] = hits_per_column

    # Iterate through the dictionary and place targets to match the number of hits for each column
    for i in range(1, len(hits) + 1):
        for j in range(1, len(hits) + 1):
            if targets[i][j] > 0:
                # If the target is already placed, skip it
                continue
            # Check if the target can be placed in the current row and column
            if targets[i - 1][j] == 0 and targets[i + 1][j] == 0 and targets[i][j - 1] == 0 and targets[i][j + 1] == 0:
                # Place the target and update the number of hits for the corresponding row and column
                targets[i][j] = 1
                targets[i - 1][j] = 1
                targets[i + 1][j] = 1
                targets[i][j - 1] = 1
                targets[i][j + 1] = 1

    # Check if all targets have been placed
    if sum(sum(targets[i].values()) for i in targets) == sum(hits):
        # Return the configuration of targets
        return targets
    else:
        # Return -1 if no valid configuration of targets exists
        return -1

