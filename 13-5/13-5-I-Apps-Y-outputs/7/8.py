
def solve(n, a):
    # Check if the wall is already complete
    if all(a[i] == a[0] for i in range(n)):
        return "YES"

    # Check if the wall can be completed with any amount of bricks
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            return "YES"

    # Check if the wall can be completed with at least one brick
    if a[0] == 1 and a[n - 1] == 1:
        return "YES"

    return "NO"

