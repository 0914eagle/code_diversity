
def get_non_similar_worlds(n, m):
    # Initialize the number of non-similar worlds to 0
    non_similar_worlds = 0
    
    # Iterate through all possible worlds
    for i in range(1, n+1):
        # Initialize the current world as an empty graph
        world = []
        
        # Add the special vertices s and t to the world
        world.append(["s", "t"])
        
        # Add the edges between the special vertices and all other vertices
        for j in range(i):
            world.append(["s", str(j+1)])
            world.append(["t", str(j+1)])
        
        # Check if the minimum cut of the current world is at least m
        if get_min_cut(world) >= m:
            # Increment the number of non-similar worlds
            non_similar_worlds += 1
    
    # Return the number of non-similar worlds
    return non_similar_worlds

def get_min_cut(world):
    # Initialize the minimum cut to 0
    min_cut = 0
    
    # Iterate through all edges in the world
    for i in range(len(world)):
        # Check if the edge is not between the special vertices s and t
        if world[i][0] != "s" and world[i][1] != "t":
            # Increment the minimum cut
            min_cut += 1
    
    # Return the minimum cut
    return min_cut

