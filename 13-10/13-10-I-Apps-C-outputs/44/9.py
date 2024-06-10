
def get_non_similar_worlds(n, m):
    # Initialize the number of non-similar worlds to 0
    non_similar_worlds = 0
    
    # Iterate through all possible worlds
    for world in range(1, n+1):
        # Check if the world satisfies the constraints
        if satisfies_constraints(world, n, m):
            # Increment the number of non-similar worlds
            non_similar_worlds += 1
    
    # Return the number of non-similar worlds
    return non_similar_worlds

def satisfies_constraints(world, n, m):
    # Initialize the number of edges to 0
    num_edges = 0
    
    # Iterate through all possible edges
    for edge in range(1, n+1):
        # Check if the edge is part of the minimum cut
        if is_part_of_minimum_cut(world, edge):
            # Increment the number of edges
            num_edges += 1
    
    # Return True if the number of edges is greater than or equal to the minimum cut, False otherwise
    return num_edges >= m

def is_part_of_minimum_cut(world, edge):
    # Check if the edge is part of the minimum cut
    if edge in world:
        return True
    else:
        return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_non_similar_worlds(n, m))

