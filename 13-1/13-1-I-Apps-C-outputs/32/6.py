
def is_valid_configuration(n, a):
    # Initialize a 2D array to store the number of targets in each row and column
    targets = [[0] * (n + 1) for _ in range(n + 1)]

    # Iterate over the number of hits for each column
    for i in range(1, n + 1):
        # Check if the number of hits is valid
        if a[i - 1] > 3:
            return False

        # Update the number of targets in each row and column
        for j in range(1, n + 1):
            if targets[j][i] == 0 and targets[j][i + 1] == 0:
                targets[j][i] = 1
                break

    # Check if all rows and columns have at most 2 targets
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if targets[i][j] > 2:
                return False

    return True


def find_configuration(n, a):
    # Initialize a 2D array to store the targets
    targets = [[0] * (n + 1) for _ in range(n + 1)]

    # Iterate over the number of hits for each column
    for i in range(1, n + 1):
        # Find a valid position for the target in the current column
        for j in range(1, n + 1):
            if targets[j][i] == 0 and targets[j][i + 1] == 0:
                targets[j][i] = 1
                break

    # Print the targets
    print(n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if targets[i][j] == 1:
                print(i, j)


n = int(input())
a = list(map(int, input().split()))

if is_valid_configuration(n, a):
    find_configuration(n, a)
else:
    print(-1)

