
def solve(targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the closest pair of targets that are not already hit
    for i in range(1, len(sorted_targets)):
        current_target = sorted_targets[i]
        if current_target[0] > last_target[0]:
            # If the current target is to the right of the last target, update the last target
            last_target = current_target
        elif current_target[0] < first_target[0]:
            # If the current target is to the left of the first target, update the first target
            first_target = current_target
        else:
            # If the current target is between the first and last target, return failure
            return "failure"

    # If all targets are hit, return success
    return "success"

