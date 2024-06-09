
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
    
    # Loop until Elsa and the father reach the goal tile or it is determined that Elsa will not be able to reach the goal
    while True:
        # Move Elsa in the current direction
        elsa_position = (elsa_position[0] + elsa_direction[0], elsa_position[1] + elsa_direction[1])
        
        # Check if Elsa has reached the goal tile
        if elsa_position == goal_tile:
            return "SUCCESS"
        
        # Check if Elsa has reached a safe tile
        if elsa_position in safe_tiles:
            # Set the direction of movement for Elsa to the opposite of the current direction
            elsa_direction = (-elsa_direction[0], -elsa_direction[1])
        else:
            # Set the direction of movement for Elsa to the opposite of the current direction
            elsa_direction = (elsa_direction[0], -elsa_direction[1])
        
        # Move the father in the current direction
        father_position = (father_position[0] + father_direction[0], father_position[1] + father_direction[1])
        
        # Check if the father has reached the goal tile
        if father_position == goal_tile:
            return "NO CHANCE"
        
        # Check if the father has reached a safe tile
        if father_position in safe_tiles:
            # Set the direction of movement for the father to the opposite of the current direction
            father_direction = (-father_direction[0], -father_direction[1])
        else:
            # Set the direction of movement for the father to the opposite of the current direction
            father_direction = (father_direction[0], -father_direction[1])
        
        # Check if Elsa will not be able to reach the goal
        if elsa_position[0] < 0 or elsa_position[0] >= map_height or elsa_position[1] < 0 or elsa_position[1] >= map_width:
            return "NO WAY"
    
    return "GO FOR IT"

