djacent(tile1, tile2):
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, path, visited, row, col):
    if len(path) == len(s):
        return True
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 13 and (new_row, new_col) not in visited:
                if is_adjacent(grid[row][col], grid[new_row][new_col]) and grid[new_row][new_col] == s[len(path)]:
                    path.append(grid[new_row][new_col])
                    visited.add((new_row, new_col))
                    if find_path(grid, s, path, visited, new_row, new_col):
                        return True
                    path.pop()
                    visited.remove((new_row, new_col))
    return False

def construct_grid(s):
    grid = [['' for _ in range(13)] for _ in range(2)]
    for i in range(13):
        grid[0][i] = s[i]
        grid[1][i] = s[i + 13]
    
    for i in range(13):
        path = [grid[0][i]]
        visited = {(0, i)}
        if find_path(grid, s, path, visited, 0, i):
            return grid, path
    return None

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    s = input().strip()
    result = construct_grid(s)
    if result:
        grid, path = result
        print_grid(grid)
    else:
        print("Impossible"