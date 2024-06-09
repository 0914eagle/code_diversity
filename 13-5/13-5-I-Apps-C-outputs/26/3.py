
def solve(x, y):
    if x == 1 and y == 1:
        return "Impossible"
    if x == 1 or y == 1:
        return "1A" * (x - 1) + "1B" * (y - 1)
    if x == 2 or y == 2:
        return "Impossible"
    if x == 3 and y == 2:
        return "1A1B"
    if x == 2 and y == 3:
        return "1B1A"
    return "Impossible"

