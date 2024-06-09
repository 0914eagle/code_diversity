
import math

def get_grid(w, h, u, d, l, r):
    grid = []
    for i in range(h):
        row = []
        for j in range(w):
            if i == 0:
                row.append('T' if j % 2 == 0 else '.')
            else:
                row.append('X' if j % 2 == 0 else '.')
        grid.append(row)
    return grid

def simulate_ball(grid, u, d, l, r):
    visited = set()
    ball_x = 0
    ball_y = 0
    while True:
        visited.add((ball_x, ball_y))
        if grid[ball_y][ball_x] == 'T':
            return True
        if grid[ball_y][ball_x] == 'X':
            return False
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        direction = directions[int(math.floor(u * 100))]
        ball_x += direction[0]
        ball_y += direction[1]
        if ball_x < 0 or ball_x >= w or ball_y < 0 or ball_y >= h:
            return False
        u = u - (u * 100) // 100
        d = d - (d * 100) // 100
        l = l - (l * 100) // 100
        r = r - (r * 100) // 100
    return False

def get_probability(grid, u, d, l, r):
    total_visits = 0
    hits = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                total_visits += 1
                if simulate_ball(grid, u, d, l, r):
                    hits += 1
    return hits / total_visits

def main():
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    grid = get_grid(w, h, u, d, l, r)
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                print(get_probability(grid, u, d, l, r))

if __name__ == '__main__':
    main()

