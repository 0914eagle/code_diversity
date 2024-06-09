
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = {}
    for i in range(n):
        game_state[i] = cuboids[i]
    
    # Play the game
    while len(game_state) > 1:
        # Determine the current player
        if player == "RUBEN":
            player = "ALBERT"
        else:
            player = "RUBEN"
        
        # Determine the move for the current player
        move = determine_move(game_state)
        
        # Apply the move to the game state
        game_state = apply_move(game_state, move)
    
    # Return the winner
    return player

def determine_move(game_state):
    # Determine the largest cuboid in the game state
    largest_cuboid = None
    for i in game_state:
        if largest_cuboid is None or game_state[i][0] * game_state[i][1] * game_state[i][2] > largest_cuboid[0] * largest_cuboid[1] * largest_cuboid[2]:
            largest_cuboid = game_state[i]
    
    # Determine the move for the largest cuboid
    move = (largest_cuboid[0] // 2, largest_cuboid[1] // 2, largest_cuboid[2] // 2)
    
    return move

def apply_move(game_state, move):
    # Apply the move to the game state
    new_game_state = {}
    for i in game_state:
        x, y, z = game_state[i]
        new_x = x - move[0]
        new_y = y - move[1]
        new_z = z - move[2]
        if new_x > 0 and new_y > 0 and new_z > 0:
            new_game_state[i] = (new_x, new_y, new_z)
    
    return new_game_state

