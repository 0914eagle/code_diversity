
def solve(n, sx, sy, dx, dy, t):
    x, y = sx, sy
    for _ in range(t):
        x = (x + dx - 1) % n + 1
        y = (y + dy - 1) % n + 1
        dx += x
        dy += y
    return x, y

