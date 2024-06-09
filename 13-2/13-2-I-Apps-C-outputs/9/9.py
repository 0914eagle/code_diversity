
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize variables
    start_position = None
    goal_position = None
    safe_tiles = []
    lava_tiles = []

    # Parse the map data
    for i in range(map_height):
        for j in range(map_width):
            if map_data[i][j] == "S":
                start_position = (i, j)
            elif map_data[i][j] == "G":
                goal_position = (i, j)
            elif map_data[i][j] == "W":
                safe_tiles.append((i, j))
            elif map_data[i][j] == "B":
                lava_tiles.append((i, j))

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
        return "NO CHANCE"
    if not is_reachable(start_position, goal_position, safe_tiles, lava_tiles, father_step_length):
        return "NO CHANCE"

    # Check if Elsa can reach the goal before the father
    if is_reachable(start_position, goal_position, safe_tiles, lava_tiles, elsa_step_length) and not is_reachable(start_position, goal_position, safe_tiles, lava_tiles, father_step_length):
        return "GO FOR IT"

    # Check if the father can reach the goal before Elsa
    if is_reachable(start_position, goal_position, safe_tiles, lava_tiles, father_step_length) and not is_reachable(start_position, goal_position, safe_tiles, lava_tiles, elsa_step_length):
        return "NO CHANCE"

    # Check if they can reach the goal at the same time
    if is_reachable(start_position, goal_position, safe_tiles, lava_tiles, elsa_step_length) and is_reachable(start_position, goal_position, safe_tiles, lava_tiles, father_step_length):
        return "SUCCESS"

    return "NO WAY"

def is_reachable(start_position, goal_position, safe_tiles, lava_tiles, step_length):
    queue = [(start_position, 0)]
    visited = set()

    while queue:
        current_position, distance = queue.pop(0)
        if current_position == goal_position:
            return True
        if distance > step_length:
            continue
        for neighbor in get_neighbors(current_position, safe_tiles, lava_tiles):
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return False

def get_neighbors(position, safe_tiles, lava_tiles):
    neighbors = []
    for i in range(position[0] - 1, position[0] + 2):
        for j in range(position[1] - 1, position[1] + 2):
            if (i, j) != position and (i, j) in safe_tiles and (i, j) not in lava_tiles:
                neighbors.append((i, j))
    return neighbors

