
def f1(N, targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first and last target to be hit
    first_target = sorted_targets[0]
    last_target = sorted_targets[-1]

    # Iterate through the targets and find the first and last target that are not on the same line
    for i in range(1, N):
        current_target = sorted_targets[i]
        if current_target[1] != first_target[1]:
            last_target = current_target
            break

    # Check if the first and last target are on the same line
    if first_target[1] == last_target[1]:
        return "failure"

    # Check if the first shot hits the first target and the last shot hits the last target
    if first_target[0] < last_target[0]:
        return "success"
    else:
        return "failure"

def f2(N, targets):
    # Initialize the number of targets hit to 0
    num_targets_hit = 0

    # Iterate through the targets and check if they are hit by the laser beams
    for target in targets:
        # Check if the target is hit by the first shot
        if target[0] < 0:
            num_targets_hit += 1

        # Check if the target is hit by the last shot
        if target[0] > 0:
            num_targets_hit += 1

    # Check if all the targets are hit
    if num_targets_hit == N:
        return "success"
    else:
        return "failure"

if __name__ == '__main__':
    N = int(input())
    targets = []
    for i in range(N):
        x, y = map(int, input().split())
        targets.append((x, y))
    print(f1(N, targets))
    print(f2(N, targets))

