
def solve(height, width, grid, i, j):
    total_water = 0
    visited = set()
    queue = [(i, j)]

    while queue:
        current_i, current_j = queue.pop(0)
        visited.add((current_i, current_j))

        for neighbor in get_neighbors(current_i, current_j, height, width):
            if neighbor not in visited and grid[neighbor[0]][neighbor[1]] < 0:
                queue.append(neighbor)
                total_water += abs(grid[neighbor[0]][neighbor[1]])

    return total_water

def get_neighbors(i, j, height, width):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < height-1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < width-1:
        neighbors.append((i, j+1))
    return neighbors

