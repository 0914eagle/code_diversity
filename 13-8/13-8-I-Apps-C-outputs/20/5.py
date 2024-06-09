
def solve(grid, i, j):
    # Initialize the total volume of water drained to 0
    total_volume = 0

    # Iterate through the grid and find all the cells that are connected to the draining device
    queue = [(i, j)]
    visited = set()
    while queue:
        i, j = queue.pop(0)
        if (i, j) not in visited:
            visited.add((i, j))
            total_volume += grid[i - 1][j - 1]
            for neighbor in get_neighbors(grid, i, j):
                queue.append(neighbor)

    return total_volume

def get_neighbors(grid, i, j):
    neighbors = []
    if i > 1 and grid[i - 2][j - 1] < 0:
        neighbors.append((i - 1, j))
    if i < len(grid) and grid[i][j - 1] < 0:
        neighbors.append((i + 1, j))
    if j > 1 and grid[i - 1][j - 2] < 0:
        neighbors.append((i, j - 1))
    if j < len(grid[0]) and grid[i - 1][j] < 0:
        neighbors.append((i, j + 1))
    return neighbors

def main():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    i, j = map(int, input().split())
    print(solve(grid, i, j))

if __name__ == "__main__":
    main()

