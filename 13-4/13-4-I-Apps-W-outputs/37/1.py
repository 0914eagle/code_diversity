
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = cuboids
    
    # Play the game
    while len(game_state) > 0:
        # Choose a cuboid to cut
        cuboid_to_cut = game_state[0]
        
        # Cut the cuboid into smaller cuboids
        smaller_cuboids = cut_cuboid(cuboid_to_cut)
        
        # Remove the original cuboid from the game state
        game_state.remove(cuboid_to_cut)
        
        # Add the smaller cuboids to the game state
        game_state.extend(smaller_cuboids)
    
    # Return the name of the winner
    return player

def cut_cuboid(cuboid):
    # Initialize the list of smaller cuboids
    smaller_cuboids = []
    
    # Cut the cuboid into smaller cuboids
    for i in range(1, cuboid[0] + 1):
        for j in range(1, cuboid[1] + 1):
            for k in range(1, cuboid[2] + 1):
                smaller_cuboids.append([i, j, k])
    
    # Return the list of smaller cuboids
    return smaller_cuboids

