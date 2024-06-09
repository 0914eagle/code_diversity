
def solve(n, sx, sy, dx, dy, t):
    x, y = sx, sy
    for _ in range(t):
        x += dx
        y += dy
        dx += x % n
        dy += y % n
    return x % n, y % n

