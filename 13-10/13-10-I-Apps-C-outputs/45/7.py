
import math

def read_input():
    N = int(input())
    lamps = []
    for _ in range(N):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    return N, lamps

def create_grid(N, lamps):
    grid = [[0] * (N + 1) for _ in range(N + 1)]
    for x, y, e in lamps:
        grid[x][y] = e
    return grid

def find_closest_pair(grid, target):
    min_diff = float('inf')
    min_pair = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == target:
                for k in range(len(grid)):
                    for l in range(len(grid[0])):
                        if grid[k][l] == -target and abs(i - k) + abs(j - l) < min_diff:
                            min_diff = abs(i - k) + abs(j - l)
                            min_pair = (i, j, k, l)
    return min_pair

def find_shortest_line(grid, closest_pair):
    x1, y1, x2, y2 = closest_pair
    dx = x2 - x1
    dy = y2 - y1
    GCD = math.gcd(dx, dy)
    dx //= GCD
    dy //= GCD
    x3 = x1 + dx
    y3 = y1 + dy
    x4 = x2 + dx
    y4 = y2 + dy
    line_length = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    return line_length

def solve(N, lamps):
    grid = create_grid(N, lamps)
    closest_pair = find_closest_pair(grid, 1)
    if closest_pair is None:
        return "IMPOSSIBLE"
    line_length = find_shortest_line(grid, closest_pair)
    return line_length

if __name__ == '__main__':
    N, lamps = read_input()
    print(solve(N, lamps))

