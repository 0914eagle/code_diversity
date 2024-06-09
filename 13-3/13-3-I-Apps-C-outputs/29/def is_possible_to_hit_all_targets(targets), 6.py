
def is_possible_to_hit_all_targets(targets):
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

    # Check if the last target is the last target in the list
    if last_target == sorted_targets[-1]:
        return "failure"

    # Check if the first shot hits the first target and the second shot hits the last target
    if first_target[0] == sorted_targets[0][0] and last_target[0] == sorted_targets[-1][0]:
        return "success"

    # If none of the above conditions are met, return "failure"
    return "failure"

