
def solve():
    H, N = map(int, input().split())
    spells = []
    for i in range(N):
        A, B = map(int, input().split())
        spells.append((A, B))

    # Sort the spells in descending order of their cost
    spells.sort(key=lambda x: x[1], reverse=True)

    # Initialize the minimum total Magic Points to 0
    min_points = 0

    # Loop through the spells and cast them until the monster's health becomes 0 or below
    for A, B in spells:
        min_points += B
        H -= A
        if H <= 0:
            break

    return min_points

