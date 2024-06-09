
def solve(targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the closest pair of targets that are not adjacent
    for i in range(1, len(sorted_targets) - 1):
        current_target = sorted_targets[i]
        if current_target[0] - last_target[0] > first_target[0] - current_target[0]:
            first_target = current_target
        if current_target[0] - first_target[0] > last_target[0] - current_target[0]:
            last_target = current_target

    # Check if the first and last target are adjacent
    if last_target[0] - first_target[0] == 1:
        return "success"
    else:
        return "failure"

