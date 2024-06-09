
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
            # If the current tile is the goal tile, set the game state to "success"
            if map_data[i][j] == "G":
                game_state = "success"
                break
                
            # If the current tile is a lava tile, set the game state to "no chance"
            if map_data[i][j] == "B":
                game_state = "no chance"
                break
                
            # If the current tile is a safe tile, update the position of Elsa and the father
            if map_data[i][j] == "W":
                # Update the position of Elsa
                elsa_position = (j, i)
                elsa_steps += 1
                
                # Update the position of the father
                father_position = (j, i)
                father_steps += 1
                
                # If the father's step length is greater than the elsa's step length, update the father's position
                if father_step_length > elsa_step_length:
                    father_position = (j + father_step_length, i)
                    father_steps += father_step_length
                
                # If the father's step length is less than the elsa's step length, update the elsa's position
                if father_step_length < elsa_step_length:
                    elsa_position = (j + elsa_step_length, i)
                    elsa_steps += elsa_step_length
                
                # If the father's step length is equal to the elsa's step length, update both positions
                if father_step_length == elsa_step_length:
                    elsa_position = (j + elsa_step_length, i)
                    father_position = (j + father_step_length, i)
                    elsa_steps += elsa_step_length
                    father_steps += father_step_length
                    
    # If the game state is still "in progress", check if Elsa has reached the goal
    if game_state == "in progress":
        if elsa_position == (map_width-1, map_height-1):
            game_state = "success"
        else:
            game_state = "go for it"
            
    # If the game state is "success", return "success"
    if game_state == "success":
        return "SUCCESS"
    
    # If the game state is "no chance", return "no chance"
    if game_state == "no chance":
        return "NO CHANCE"
    
    # If the game state is "go for it", return "go for it"
    if game_state == "go for it":
        return "GO FOR IT"
    
    # If the game state is "in progress" and neither Elsa nor the father has reached the goal, return "no way"
    return "NO WAY"

