
def solve(player, num_cuboids, *cuboid_sizes):
    # Initialize the game state with the given cuboids
    game_state = set(cuboid_sizes)
    
    # Play the game until one player wins
    while len(game_state) > 0:
        # Choose a cuboid to cut
        cuboid = game_state.pop()
        
        # Cut the cuboid into smaller cuboids
        smaller_cuboids = cut_cuboid(cuboid)
        
        # Add the smaller cuboids to the game state
        game_state.update(smaller_cuboids)
    
    # Return the name of the winning player
    return player

def cut_cuboid(cuboid):
    # Cut the cuboid into smaller cuboids
    smaller_cuboids = []
    for i in range(1, cuboid[0] + 1):
        for j in range(1, cuboid[1] + 1):
            for k in range(1, cuboid[2] + 1):
                smaller_cuboids.append((i, j, k))
    
    return smaller_cuboids

