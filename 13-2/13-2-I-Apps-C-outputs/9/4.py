
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the starting position of Elsa and the father
    elsa_position = (0, 0)
    father_position = (0, 0)
    
    # Initialize the set of safe tiles
    safe_tiles = set()
    
    # Loop through the map data and add the safe tiles to the set
    for i in range(map_height):
        for j in range(map_width):
            if map_data[i][j] == "W":
                safe_tiles.add((i, j))
    
    # Find the position of the start and goal tiles
    start_tile = None
    goal_tile = None
    for i in range(map_height):
        for j in range(map_width):
            if map_data[i][j] == "S":
                start_tile = (i, j)
            elif map_data[i][j] == "G":
                goal_tile = (i, j)
    
    # Set the initial direction of movement for Elsa and the father
    elsa_direction = (0, 1)
    father_direction = (0, 1)
    
    # Loop until Elsa and the father reach the goal tile or it is determined that Elsa will not reach the goal
    while elsa_position != goal_tile and father_position != goal_tile:
        # Move Elsa in the current direction
        elsa_position = (elsa_position[0] + elsa_direction[0], elsa_position[1] + elsa_direction[1])
        
        # If Elsa reaches a safe tile, change direction randomly
        if elsa_position in safe_tiles:
            elsa_direction = (random.randint(-1, 1), random.randint(-1, 1))
        
        # Move the father in the current direction
        father_position = (father_position[0] + father_direction[0], father_position[1] + father_direction[1])
        
        # If the father reaches a safe tile, change direction randomly
        if father_position in safe_tiles:
            father_direction = (random.randint(-1, 1), random.randint(-1, 1))
    
    # Check if Elsa and the father reach the goal at the same time
    if elsa_position == goal_tile and father_position == goal_tile:
        return "SUCCESS"
    
    # Check if Elsa reaches the goal before the father
    elif elsa_position == goal_tile:
        return "GO FOR IT"
    
    # Check if the father reaches the goal before Elsa
    elif father_position == goal_tile:
        return "NO CHANCE"
    
    # If neither Elsa nor the father reaches the goal, return "NO WAY"
    else:
        return "NO WAY"

