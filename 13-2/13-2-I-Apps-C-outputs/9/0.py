
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the starting position of Elsa and the father
    elsa_position = (0, 0)
    father_position = (0, 0)
    
    # Initialize the number of steps taken by Elsa and the father
    elsa_steps = 0
    father_steps = 0
    
    # Initialize the game state as "in progress"
    game_state = "in progress"
    
    # Loop through each row of the map
    for i in range(map_height):
        # Loop through each column of the map
        for j in range(map_width):
            # Check if the current tile is safe or lava
            if map_data[i][j] == "W":
                # If the current tile is safe, check if Elsa or the father can move to it
                if elsa_position[0] + elsa_step_length >= i and elsa_position[1] + elsa_step_length >= j and elsa_position[0] - elsa_step_length <= i and elsa_position[1] - elsa_step_length <= j:
                    # If Elsa can move to the current tile, update her position and number of steps taken
                    elsa_position = (i, j)
                    elsa_steps += 1
                if father_position[0] + father_step_length >= i and father_position[1] + father_step_length >= j and father_position[0] - father_step_length <= i and father_position[1] - father_step_length <= j:
                    # If the father can move to the current tile, update his position and number of steps taken
                    father_position = (i, j)
                    father_steps += 1
            elif map_data[i][j] == "G":
                # If the current tile is the goal, check if Elsa or the father can reach it
                if elsa_position[0] == i and elsa_position[1] == j:
                    # If Elsa can reach the goal, update the game state and break out of the loops
                    game_state = "success"
                    break
                elif father_position[0] == i and father_position[1] == j:
                    # If the father can reach the goal, update the game state and break out of the loops
                    game_state = "go for it"
                    break
    
    # If the game is still in progress, check if Elsa or the father can reach the goal from their current position
    if game_state == "in progress":
        # Check if Elsa can reach the goal from her current position
        if elsa_position[0] + elsa_step_length >= map_height - 1 and elsa_position[1] + elsa_step_length >= map_width - 1 and elsa_position[0] - elsa_step_length <= map_height - 1 and elsa_position[1] - elsa_step_length <= map_width - 1:
            # If Elsa can reach the goal, update the game state
            game_state = "success"
        # Check if the father can reach the goal from his current position
        elif father_position[0] + father_step_length >= map_height - 1 and father_position[1] + father_step_length >= map_width - 1 and father_position[0] - father_step_length <= map_height - 1 and father_position[1] - father_step_length <= map_width - 1:
            # If the father can reach the goal, update the game state
            game_state = "go for it"
    
    # Return the game state
    return game_state

