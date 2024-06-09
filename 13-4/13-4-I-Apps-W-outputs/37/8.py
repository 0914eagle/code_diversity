
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = {}
    for i in range(n):
        game_state[i] = cuboids[i]
    
    # Game loop
    while len(game_state) > 0:
        # Choose a cuboid to cut
        cuboid_id = choose_cuboid(game_state)
        cuboid = game_state[cuboid_id]
        
        # Cut the cuboid
        cut_planes = choose_cut_planes(cuboid)
        new_cuboids = cut_cuboid(cuboid, cut_planes)
        
        # Update the game state
        for new_cuboid in new_cuboids:
            game_state[len(game_state)] = new_cuboid
        
        # Remove the original cuboid
        del game_state[cuboid_id]
    
    # Determine the winner
    if player == "RUBEN":
        return "RUBEN"
    else:
        return "ALBERT"

def choose_cuboid(game_state):
    # Choose the cuboid with the largest volume
    max_volume = -1
    chosen_cuboid_id = -1
    for cuboid_id in game_state:
        cuboid = game_state[cuboid_id]
        volume = cuboid[0] * cuboid[1] * cuboid[2]
        if volume > max_volume:
            max_volume = volume
            chosen_cuboid_id = cuboid_id
    
    return chosen_cuboid_id

def choose_cut_planes(cuboid):
    # Choose the cut planes that result in the most new cuboids
    max_new_cuboids = -1
    chosen_cut_planes = []
    for x in range(1, cuboid[0] + 1):
        for y in range(1, cuboid[1] + 1):
            for z in range(1, cuboid[2] + 1):
                new_cuboids = cut_cuboid(cuboid, [x, y, z])
                if len(new_cuboids) > max_new_cuboids:
                    max_new_cuboids = len(new_cuboids)
                    chosen_cut_planes = [x, y, z]
    
    return chosen_cut_planes

def cut_cuboid(cuboid, cut_planes):
    # Cut the cuboid and return the new cuboids
    new_cuboids = []
    for x in range(1, cuboid[0] + 1):
        for y in range(1, cuboid[1] + 1):
            for z in range(1, cuboid[2] + 1):
                if x == cut_planes[0] and y == cut_planes[1] and z == cut_planes[2]:
                    continue
                new_cuboid = [x, y, z]
                new_cuboids.append(new_cuboid)
    
    return new_cuboids

