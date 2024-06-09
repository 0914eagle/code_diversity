
def solve(player, n, cuboids):
    # Initialize the game state with the given cuboids
    game_state = cuboids
    
    # Play the game until one player has no more cuboids
    while len(game_state) > 0:
        # Choose a cuboid to cut
        cuboid_to_cut = choose_cuboid(game_state)
        
        # Cut the cuboid into smaller cuboids
        smaller_cuboids = cut_cuboid(cuboid_to_cut)
        
        # Remove the original cuboid from the game state
        game_state.remove(cuboid_to_cut)
        
        # Add the smaller cuboids to the game state
        game_state.extend(smaller_cuboids)
        
        # Switch players
        player = "RUBEN" if player == "ALBERT" else "ALBERT"
    
    # Return the name of the winner
    return player

def choose_cuboid(game_state):
    # Choose the cuboid with the smallest volume
    return min(game_state, key=lambda x: x[0] * x[1] * x[2])

def cut_cuboid(cuboid):
    # Cut the cuboid into smaller cuboids
    smaller_cuboids = []
    for i in range(1, cuboid[0] + 1):
        for j in range(1, cuboid[1] + 1):
            for k in range(1, cuboid[2] + 1):
                if i != cuboid[0] and j != cuboid[1] and k != cuboid[2]:
                    smaller_cuboids.append([i, j, k])
    
    return smaller_cuboids

