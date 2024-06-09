
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the start and goal positions
    start_position = (0, 0)
    goal_position = (map_width - 1, map_height - 1)
    
    # Initialize the visited matrix to keep track of the safe tiles
    visited = [[False for _ in range(map_width)] for _ in range(map_height)]
    
    # Mark the start and goal tiles as safe
    visited[start_position[0]][start_position[1]] = True
    visited[goal_position[0]][goal_position[1]] = True
    
    # Initialize the queue with the start position
    queue = [start_position]
    
    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        current_position = queue.pop(0)
        
        # Check if the current position is the goal position
        if current_position == goal_position:
            return "SUCCESS"
        
        # Get the safe tiles that are reachable from the current position
        safe_tiles = get_safe_tiles(current_position, map_width, map_height, map_data, visited)
        
        # Add the safe tiles to the queue
        for safe_tile in safe_tiles:
            queue.append(safe_tile)
            visited[safe_tile[0]][safe_tile[1]] = True
    
    # If the queue is empty, return "NO WAY"
    return "NO WAY"

def get_safe_tiles(current_position, map_width, map_height, map_data, visited):
    # Initialize the list of safe tiles
    safe_tiles = []
    
    # Get the current tile type
    current_tile_type = map_data[current_position[0]][current_position[1]]
    
    # Check if the current tile is safe
    if current_tile_type == "W":
        safe_tiles.append(current_position)
    
    # Get the possible moves for the current position
    possible_moves = get_possible_moves(current_position, map_width, map_height, visited)
    
    # Add the possible moves to the list of safe tiles
    for move in possible_moves:
        safe_tiles.append(move)
    
    return safe_tiles

def get_possible_moves(current_position, map_width, map_height, visited):
    # Initialize the list of possible moves
    possible_moves = []
    
    # Get the current tile type
    current_tile_type = map_data[current_position[0]][current_position[1]]
    
    # Check if the current tile is safe
    if current_tile_type == "W":
        # Get the possible moves for the current position
        possible_moves = [(current_position[0] + 1, current_position[1]),
                          (current_position[0] - 1, current_position[1]),
                          (current_position[0], current_position[1] + 1),
                          (current_position[0], current_position[1] - 1)]
        
        # Filter out the moves that are not within the map bounds or are not safe
        possible_moves = [move for move in possible_moves if 0 <= move[0] < map_width and 0 <= move[1] < map_height and visited[move[0]][move[1]] == False]
    
    return possible_moves

