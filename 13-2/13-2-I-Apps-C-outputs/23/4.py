
def f1(N, targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the first and last target that are not on the same line
    for i in range(1, N):
        current_target = sorted_targets[i]
        if current_target[1] != last_target[1]:
            last_target = current_target
            break

    # Check if the first and last target are on the same line
    if first_target[1] == last_target[1]:
        return "failure"

    # Check if the first and last target are on opposite sides of the line
    if first_target[0] * last_target[0] < 0:
        return "success"

    # Check if the first and last target are on the same side of the line
    if first_target[0] * last_target[0] > 0:
        return "failure"

    # Check if the first and last target are on the same line
    if first_target[1] == last_target[1]:
        return "success"

    # If none of the above conditions are met, the first and last target are not on the same line
    return "failure"

def f2(N, targets):
    # Initialize the number of targets hit to 0
    num_targets_hit = 0

    # Iterate through the targets and check if they are hit by the laser beams
    for target in targets:
        # Check if the target is hit by the first laser beam
        if target[0] >= 0 and target[1] >= 0:
            num_targets_hit += 1

        # Check if the target is hit by the second laser beam
        if target[0] <= 0 and target[1] <= 0:
            num_targets_hit += 1

    # Check if all targets are hit
    if num_targets_hit == N:
        return "success"

    # If not all targets are hit, return failure
    return "failure"

if __name__ == '__main__':
    N = int(input())
    targets = []
    for i in range(N):
        x, y = map(int, input().split())
        targets.append((x, y))
    print(f1(N, targets))
    print(f2(N, targets))

