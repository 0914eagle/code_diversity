
def f1(N, targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the closest pair of targets that are not on the same line
    for i in range(1, N-1):
        current_target = sorted_targets[i]
        if current_target[0] != last_target[0]:
            # Find the slope of the line between the current target and the last target
            slope = (current_target[1] - last_target[1]) / (current_target[0] - last_target[0])

            # Check if the slope is equal to the slope of the line between the first target and the last target
            if slope == (last_target[1] - first_target[1]) / (last_target[0] - first_target[0]):
                # If the slopes are equal, return "success"
                return "success"

    # If no pair of targets with equal slopes is found, return "failure"
    return "failure"

def f2(N, targets):
    # Initialize the first and last target to be hit
    first_target = targets[0]
    last_target = targets[-1]

    # Iterate through the targets and find the closest pair of targets that are not on the same line
    for i in range(1, N-1):
        current_target = targets[i]
        if current_target[0] != last_target[0]:
            # Find the slope of the line between the current target and the last target
            slope = (current_target[1] - last_target[1]) / (current_target[0] - last_target[0])

            # Check if the slope is equal to the slope of the line between the first target and the last target
            if slope == (last_target[1] - first_target[1]) / (last_target[0] - first_target[0]):
                # If the slopes are equal, return "success"
                return "success"

    # If no pair of targets with equal slopes is found, return "failure"
    return "failure"

if __name__ == '__main__':
    N = int(input())
    targets = []
    for i in range(N):
        x, y = map(int, input().split())
        targets.append((x, y))
    print(f1(N, targets))

