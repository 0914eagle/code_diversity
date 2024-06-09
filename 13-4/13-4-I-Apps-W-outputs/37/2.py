
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
        
        # Choose a cuboid to cut
        cuboid_to_cut = choose_cuboid(game_state)
        
        # Cut the cuboid
        new_cuboids = cut_cuboid(game_state[cuboid_to_cut])
        
        # Remove the original cuboid
        del game_state[cuboid_to_cut]
        
        # Add the new cuboids to the game state
        for i, cuboid in enumerate(new_cuboids):
            game_state[len(game_state) + i] = cuboid
    
    # Determine the winner
    if player == "RUBEN":
        return "RUBEN"
    else:
        return "ALBERT"

def choose_cuboid(game_state):
    # Choose the cuboid with the largest volume
    return max(game_state, key=lambda x: x[0] * x[1] * x[2])

def cut_cuboid(cuboid):
    # Cut the cuboid into smaller cuboids
    new_cuboids = []
    for i in range(1, cuboid[0] + 1):
        for j in range(1, cuboid[1] + 1):
            for k in range(1, cuboid[2] + 1):
                new_cuboids.append((i, j, k))
    
    return new_cuboids

