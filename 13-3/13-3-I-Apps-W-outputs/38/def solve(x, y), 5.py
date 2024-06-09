
def solve(x, y):
    if x == 0 or y == 0:
        return "Brown"
    if x < y:
        return "Alice"
    if y < x:
        return "Brown"
    return "Brown"

