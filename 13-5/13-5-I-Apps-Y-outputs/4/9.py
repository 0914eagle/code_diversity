
def solve(N, L, drawers):
    items = {}
    for i in range(N):
        item = i + 1
        drawer_a, drawer_b = drawers[i]
        if drawer_a not in items and drawer_b not in items:
            items[drawer_a] = item
        elif drawer_a in items and drawer_b not in items:
            items[drawer_b] = item
        elif drawer_a not in items and drawer_b in items:
            items[drawer_a] = item
        else:
            items[drawer_b] = item
    return ["LADICA" if item in items else "SMECE" for item in range(1, N + 1)]

