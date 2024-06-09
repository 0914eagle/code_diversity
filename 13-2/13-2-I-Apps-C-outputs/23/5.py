
def f1(N, targets):
    # Sort the targets by their x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Initialize the minimum number of shots needed to hit all targets as infinity
    min_shots = float('inf')

    # Iterate over all possible starting points for the first shot
    for i in range(N):
        # Initialize the number of shots needed for this starting point as 1
        shots = 1

        # Iterate over all targets after the starting point
        for j in range(i+1, N):
            # If the target is not on the same line as the previous target, increase the number of shots needed
            if sorted_targets[j][1] != sorted_targets[j-1][1]:
                shots += 1

        # If the number of shots needed is less than the minimum, update the minimum
        if shots < min_shots:
            min_shots = shots

    # If the minimum number of shots needed is less than or equal to 2, return "success"
    if min_shots <= 2:
        return "success"
    else:
        return "failure"

def f2(N, targets):
    # Initialize the number of shots needed as 0
    shots = 0

    # Iterate over all targets
    for i in range(N):
        # If the target is not on the same line as the previous target, increase the number of shots needed
        if i > 0 and targets[i][1] != targets[i-1][1]:
            shots += 1

    # If the number of shots needed is less than or equal to 2, return "success"
    if shots <= 2:
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

