
def is_success(targets):
    # Sort the targets by their x-coordinates
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last targets to hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and update the first and last targets to hit
    for i in range(1, len(sorted_targets)):
        current_target = sorted_targets[i]
        if current_target[0] < first_target[0]:
            first_target = current_target
        if current_target[0] > last_target[0]:
            last_target = current_target

    # Check if the first and last targets to hit are the same
    if first_target == last_target:
        return "success"
    else:
        return "failure"

