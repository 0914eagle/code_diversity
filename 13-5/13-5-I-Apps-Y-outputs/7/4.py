
def solve(n, a):
    # Check if the wall is already complete
    if all(x == a[0] for x in a):
        return "YES"

    # Check if the wall can be completed using bricks
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            return "YES"

    # Check if the wall can be completed using zero bricks
    if all(x == 1 for x in a):
        return "YES"

    # The wall cannot be completed
    return "NO"

