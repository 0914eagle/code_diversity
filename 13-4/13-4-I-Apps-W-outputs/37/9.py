
def solve(player, num_cuboids, *cuboids):
    # Initialize the game state with the given number of cuboids
    game_state = [cuboid for cuboid in cuboids]
    
    # Loop until a player has won the game
    while len(game_state) > 0:
        # Choose a player to make a move
        if player == "RUBEN":
            player = "ALBERT"
        else:
            player = "RUBEN"
        
        # Get the current player's move
        move = get_move(game_state)
        
        # Update the game state with the player's move
        game_state = update_game_state(game_state, move)
    
    # Return the name of the winning player
    return player

def get_move(game_state):
    # Choose a random cuboid from the game state
    cuboid = random.choice(game_state)
    
    # Choose random values for the three axes
    x = random.randint(1, cuboid[0])
    y = random.randint(1, cuboid[1])
    z = random.randint(1, cuboid[2])
    
    # Return the move as a tuple of the cuboid and the three axes
    return (cuboid, x, y, z)

def update_game_state(game_state, move):
    # Get the cuboid and the three axes from the move
    cuboid, x, y, z = move
    
    # Create a list of the smaller cuboids that result from cutting the cuboid
    smaller_cuboids = []
    if x > 0:
        smaller_cuboids.append((x, cuboid[1], cuboid[2]))
    if y > 0:
        smaller_cuboids.append((cuboid[0] - x, y, cuboid[2]))
    if z > 0:
        smaller_cuboids.append((cuboid[0], cuboid[1] - y, z))
    if x > 0 and y > 0:
        smaller_cuboids.append((x, y, cuboid[2]))
    if x > 0 and z > 0:
        smaller_cuboids.append((x, cuboid[1], z))
    if y > 0 and z > 0:
        smaller_cuboids.append((cuboid[0] - x, y, z))
    
    # Remove the original cuboid from the game state
    game_state.remove(cuboid)
    
    # Add the smaller cuboids to the game state
    game_state.extend(smaller_cuboids)
    
    # Return the updated game state
    return game_state

