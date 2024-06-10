djacent(tile1, tile2):
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, path, visited):
    if len(path) == len(s):
        return True

    current_tile = path[-1]
    for row in range(2):
        for col in range(13):
            tile = grid[row][col]
            if tile not in visited and is_adjacent(current_tile, tile):
                visited.add(tile)
                path.append(tile)
                if find_path(grid, s, path, visited):
                    return True
                path.pop()
                visited.remove(tile)
    return False

def construct_grid(s):
    grid = [['' for _ in range(13)] for _ in range(2)]
    for i in range(13):
        grid[0][i] = s[i]
        grid[1][i] = s[i + 13]

    for row in range(2):
        for col in range(13):
            visited = set()
            visited.add(grid[row][col])
            if find_path(grid, s, [grid[row][col]], visited):
                return grid

    return None

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    s = input().strip()
    grid = construct_grid(s)
    if grid:
        print_grid(grid)
    else:
        print("Impossible"