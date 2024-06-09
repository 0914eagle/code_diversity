
def is_valid_move(grid, row, col, organs):
    # Check if the move is valid
    if grid[row][col] != "E":
        return False
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False
    if grid[row][col] in organs:
        return False
    return True

def find_empty_space(grid, organs):
    # Find the empty space in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "E":
                return row, col
    return None, None

def get_neighbors(grid, row, col, organs):
    # Get the neighbors of the empty space
    neighbors = []
    if is_valid_move(grid, row-1, col, organs):
        neighbors.append((row-1, col))
    if is_valid_move(grid, row+1, col, organs):
        neighbors.append((row+1, col))
    if is_valid_move(grid, row, col-1, organs):
        neighbors.append((row, col-1))
    if is_valid_move(grid, row, col+1, organs):
        neighbors.append((row, col+1))
    return neighbors

def get_organ_position(grid, organ, organs):
    # Get the position of an organ in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == organ:
                return row, col
    return None, None

def get_shortest_path(grid, organs, start, goal):
    # Find the shortest path between two organs
    visited = set()
    queue = [(start, [])]
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        visited.add(current)
        for neighbor in get_neighbors(grid, *current, organs):
            if neighbor not in visited and neighbor not in queue:
                queue.append((neighbor, path + [neighbor]))
    return []

def solve(grid, organs):
    # Solve the problem
    empty_row, empty_col = find_empty_space(grid, organs)
    for organ in organs:
        organ_row, organ_col = get_organ_position(grid, organ, organs)
        path = get_shortest_path(grid, organs, (empty_row, empty_col), (organ_row, organ_col))
        if not path:
            return []
        for move in path:
            grid[move[0]][move[1]] = "E"
            empty_row, empty_col = move
    return grid

