
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = cuboids
    
    # Iterate through each cuboid
    for i in range(n):
        # Choose the cuboid to cut
        cuboid_to_cut = game_state[i]
        
        # Cut the cuboid into smaller cuboids
        smaller_cuboids = cut_cuboid(cuboid_to_cut)
        
        # Remove the original cuboid from the game state
        game_state.remove(cuboid_to_cut)
        
        # Add the smaller cuboids to the game state
        game_state.extend(smaller_cuboids)
    
    # Return the winner
    if player == "RUBEN":
        return "RUBEN"
    else:
        return "ALBERT"

def cut_cuboid(cuboid):
    # Initialize the smaller cuboids
    smaller_cuboids = []
    
    # Cut the cuboid into smaller cuboids
    for i in range(1, cuboid[0]+1):
        for j in range(1, cuboid[1]+1):
            for k in range(1, cuboid[2]+1):
                if i != cuboid[0] and j != cuboid[1] and k != cuboid[2]:
                    smaller_cuboids.append([i, j, k])
    
    # Return the smaller cuboids
    return smaller_cuboids

