
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = {cuboid: 1 for cuboid in cuboids}
    
    # Iterate through the game states
    while len(game_state) > 0:
        # Choose a cuboid to cut
        cuboid = choose_cuboid(game_state)
        
        # Cut the cuboid into smaller cuboids
        smaller_cuboids = cut_cuboid(cuboid)
        
        # Update the game state
        for smaller_cuboid in smaller_cuboids:
            game_state[smaller_cuboid] = 1
    
    # Return the winner
    return player

def choose_cuboid(game_state):
    # Choose the cuboid with the largest size
    return max(game_state, key=lambda x: x[1] * x[2] * x[3])

def cut_cuboid(cuboid):
    # Cut the cuboid into smaller cuboids
    smaller_cuboids = []
    for i in range(1, cuboid[1] + 1):
        for j in range(1, cuboid[2] + 1):
            for k in range(1, cuboid[3] + 1):
                if i != cuboid[1] and j != cuboid[2] and k != cuboid[3]:
                    smaller_cuboids.append([i, j, k])
    
    return smaller_cuboids

