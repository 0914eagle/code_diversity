
import copy

def get_neighbors(row, col, rows, cols):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < cols - 1:
        neighbors.append((row, col + 1))
    return neighbors

def bfs(grid, rows, cols, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (row, col), time = queue.pop(0)
        if (row, col) == end:
            return time
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for neighbor in get_neighbors(row, col, rows, cols):
            if grid[neighbor[0]][neighbor[1]] != 'X' and neighbor not in visited:
                queue.append((neighbor, time + 1))
    return -1

def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'D':
                end = (row, col)
    if start is None or end is None:
        return -1
    return bfs(grid, rows, cols, start, end)

def main():
    rows, cols = map(int, input().split())
    grid = [input() for _ in range(rows)]
    print(solve(grid))

if __name__ == '__main__':
    main()

