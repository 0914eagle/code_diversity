
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

            # Find the y-intercept of the line
            y_intercept = current_target[1] - slope * current_target[0]

            # Check if the first target is on the line defined by the current target and the last target
            if first_target[1] == slope * first_target[0] + y_intercept:
                return "success"

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

            # Find the y-intercept of the line
            y_intercept = current_target[1] - slope * current_target[0]

            # Check if the first target is on the line defined by the current target and the last target
            if first_target[1] == slope * first_target[0] + y_intercept:
                return "success"

    return "failure"

if __name__ == '__main__':
    N = int(input())
    targets = []
    for i in range(N):
        x, y = map(int, input().split())
        targets.append((x, y))
    print(f1(N, targets))
    print(f2(N, targets))

