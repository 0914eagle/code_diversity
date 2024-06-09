
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize variables
    start_position = None
    goal_position = None
    safe_tiles = []
    lava_tiles = []

    # Parse the map data
    for row in range(map_height):
        for col in range(map_width):
            tile = map_data[row][col]
            if tile == "S":
                start_position = (row, col)
            elif tile == "G":
                goal_position = (row, col)
            elif tile == "W":
                safe_tiles.append((row, col))
            elif tile == "B":
                lava_tiles.append((row, col))

    # Check if start and goal positions are valid
    if start_position is None or goal_position is None:
        return "NO WAY"

    # Check if Elsa can reach the goal
    if elsa_step_length >= map_width or elsa_step_length >= map_height:
        return "NO CHANCE"
    if not is_reachable(start_position, goal_position, safe_tiles, lava_tiles, elsa_step_length):
        return "NO CHANCE"

    # Check if the father can reach the goal
    if father_step_length >= map_width or father_step_length >= map_height:
        return "GO FOR IT"
    if not is_reachable(start_position, goal_position, safe_tiles, lava_tiles, father_step_length):
        return "GO FOR IT"

    # Check if Elsa and the father can reach the goal at the same time
    if is_reachable(start_position, goal_position, safe_tiles, lava_tiles, min(elsa_step_length, father_step_length)):
        return "SUCCESS"

    # If none of the above conditions are met, return "NO WAY"
    return "NO WAY"

# Check if a position is reachable from a start position
def is_reachable(start_position, goal_position, safe_tiles, lava_tiles, step_length):
    queue = [(start_position, 0)]
    visited = set()
    while queue:
        position, distance = queue.pop(0)
        if position == goal_position:
            return True
        if distance > step_length:
            continue
        for neighbor in get_neighbors(position, safe_tiles, lava_tiles):
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)
    return False

# Get the neighbors of a position
def get_neighbors(position, safe_tiles, lava_tiles):
    row, col = position
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < len(safe_tiles) and 0 <= nc < len(safe_tiles[0]):
            neighbors.append((nr, nc))
    return neighbors

