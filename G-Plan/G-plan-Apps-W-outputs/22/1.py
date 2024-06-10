djacent(tile1, tile2):
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, path):
    if not s:
        return True
    for i in range(2):
        for j in range(13):
            if grid[i][j] == s[0] and (not path or is_adjacent(path[-1], grid[i][j])):
                path.append(grid[i][j])
                if find_path(grid, s[1:], path):
                    return True
                path.pop()
    return False

def generate_grid(s):
    grid = [['' for _ in range(13)] for _ in range(2)]
    for i in range(2):
        for j in range(13):
            grid[i][j] = s[i * 13 + j]
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def solve_problem(s):
    grid = generate_grid(s)
    path = []
    if find_path(grid, s, path):
        print_grid(grid)
    else:
        print("Impossible")

if __name__ == "__main__":
    s = input().strip()
    solve_problem(s)
