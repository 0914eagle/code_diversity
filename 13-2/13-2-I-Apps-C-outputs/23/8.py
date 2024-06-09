
def f1(N, targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the first shot
    first_shot = (sorted_targets[0][0], sorted_targets[0][1])

    # Initialize the second shot
    second_shot = (sorted_targets[-1][0], sorted_targets[-1][1])

    # Loop through the targets and check if they can be hit with the two shots
    for i in range(1, N):
        # Check if the current target is between the first and second shot
        if first_shot[0] < sorted_targets[i][0] < second_shot[0]:
            # If it is, update the first shot to be the current target
            first_shot = (sorted_targets[i][0], sorted_targets[i][1])
        elif first_shot[0] > sorted_targets[i][0] > second_shot[0]:
            # If it is, update the second shot to be the current target
            second_shot = (sorted_targets[i][0], sorted_targets[i][1])
        else:
            # If the current target cannot be hit with the two shots, return failure
            return "failure"

    # If all targets have been hit, return success
    return "success"

def f2(N, targets):
    # Initialize the first shot
    first_shot = (targets[0][0], targets[0][1])

    # Initialize the second shot
    second_shot = (targets[-1][0], targets[-1][1])

    # Loop through the targets and check if they can be hit with the two shots
    for i in range(1, N):
        # Check if the current target is between the first and second shot
        if first_shot[0] < targets[i][0] < second_shot[0]:
            # If it is, update the first shot to be the current target
            first_shot = (targets[i][0], targets[i][1])
        elif first_shot[0] > targets[i][0] > second_shot[0]:
            # If it is, update the second shot to be the current target
            second_shot = (targets[i][0], targets[i][1])
        else:
            # If the current target cannot be hit with the two shots, return failure
            return "failure"

    # If all targets have been hit, return success
    return "success"

if __name__ == '__main__':
    N = int(input())
    targets = []
    for i in range(N):
        x, y = map(int, input().split())
        targets.append((x, y))
    print(f1(N, targets))

