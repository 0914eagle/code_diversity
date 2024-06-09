
def is_successful(targets):
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

    # If the last target is not the last target in the list, return failure
    if last_target != sorted_targets[-1]:
        return "failure"

    # Otherwise, return success
    return "success"

