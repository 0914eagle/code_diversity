
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the starting position of Elsa and the father
    elsa_position = (0, 0)
    father_position = (0, 0)
    
    # Initialize the number of steps taken by Elsa and the father
    elsa_steps = 0
    father_steps = 0
    
    # Initialize the game state as "in progress"
    game_state = "in progress"
    
    # Loop through each tile in the map
    for i in range(map_height):
        for j in range(map_width):
            # If the current tile is the start tile, set the starting position of Elsa and the father
            if map_data[i][j] == "S":
                elsa_position = (i, j)
                father_position = (i, j)
            
            # If the current tile is the goal tile, set the game state to "success"
            elif map_data[i][j] == "G":
                game_state = "success"
            
            # If the current tile is a lava tile, set the game state to "no chance"
            elif map_data[i][j] == "B":
                game_state = "no chance"
            
            # If the game state is "in progress", check if Elsa or the father can move to the current tile
            if game_state == "in progress":
                # Check if Elsa can move to the current tile
                if map_data[i][j] == "W" and elsa_steps < elsa_step_length:
                    elsa_position = (i, j)
                    elsa_steps += 1
                
                # Check if the father can move to the current tile
                if map_data[i][j] == "W" and father_steps < father_step_length:
                    father_position = (i, j)
                    father_steps += 1
                
                # If both Elsa and the father can move to the current tile, set the game state to "go for it"
                if elsa_position == father_position:
                    game_state = "go for it"
                
                # If either Elsa or the father cannot move to the current tile, set the game state to "no way"
                if elsa_position != father_position:
                    game_state = "no way"
    
    # Return the game state
    return game_state

