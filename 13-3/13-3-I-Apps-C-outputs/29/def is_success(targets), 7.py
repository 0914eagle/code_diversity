
def is_success(targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the closest target to the first target that is not the last target
    for i in range(1, len(sorted_targets) - 1):
        current_target = sorted_targets[i]
        if current_target[0] > first_target[0] and current_target[0] < last_target[0]:
            last_target = current_target
            break

    # Check if the last target is the same as the first target
    if first_target == last_target:
        return "failure"

    # Check if the targets are on a straight line
    if first_target[1] != last_target[1]:
        return "failure"

    # Check if the targets are within the range of the laser beam
    if abs(first_target[0] - last_target[0]) > 2:
        return "failure"

    return "success"

