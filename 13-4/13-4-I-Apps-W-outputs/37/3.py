
def solve(player, num_cuboids, *cuboids):
    # Initialize the game state with the given cuboids
    game_state = cuboids
    
    # Loop through each cuboid and find the player who can make the next move
    while len(game_state) > 0:
        # Find the player who can make the next move
        if player == "RUBEN":
            player = "ALBERT"
        else:
            player = "RUBEN"
        
        # Find the largest cuboid that can be cut
        largest_cuboid = find_largest_cuboid(game_state)
        
        # Cut the largest cuboid and update the game state
        game_state = cut_cuboid(game_state, largest_cuboid)
    
    # Return the name of the player who wins the game
    return player

def find_largest_cuboid(cuboids):
    # Find the largest cuboid by comparing the volume of each cuboid
    largest_cuboid = None
    for cuboid in cuboids:
        if largest_cuboid is None or cuboid[0] * cuboid[1] * cuboid[2] > largest_cuboid[0] * largest_cuboid[1] * largest_cuboid[2]:
            largest_cuboid = cuboid
    
    return largest_cuboid

def cut_cuboid(cuboids, cuboid):
    # Cut the largest cuboid into smaller cuboids and return the updated game state
    x, y, z = cuboid
    new_cuboids = []
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                new_cuboids.append((i, j, k))
    
    return [cuboid for cuboid in cuboids if cuboid not in new_cuboids]

