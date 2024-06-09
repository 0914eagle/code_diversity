
def solve(x, y):
    if x == 1 and y == 1:
        return "Impossible"
    if x == 1 and y > 1:
        return "B" * (y - 1)
    if y == 1 and x > 1:
        return "A" * (x - 1)
    if x > 1 and y > 1:
        return "AB"

