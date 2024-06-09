
def solve(X, Y):
    if X == 0 or Y == 0:
        return "Brown"
    if X < Y:
        return "Alice"
    if Y < X:
        return "Brown"
    return "Alice"

