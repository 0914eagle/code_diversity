
def get_number_of_non_similar_worlds(n, m):
    # Initialize the number of non-similar worlds to 0
    non_similar_worlds = 0
    
    # Iterate through all possible worlds
    for i in range(1, 2**n):
        # Convert the binary representation of i to a list of bits
        world = [int(j) for j in bin(i)[2:]]
        
        # Check if the world satisfies the constraints
        if is_valid_world(world, n, m):
            # Increment the number of non-similar worlds
            non_similar_worlds += 1
    
    # Return the number of non-similar worlds
    return non_similar_worlds % (10**9 + 7)

def is_valid_world(world, n, m):
    # Initialize the number of edges to 0
    edges = 0
    
    # Iterate through each pair of vertices in the world
    for i in range(n):
        for j in range(i+1, n):
            # Check if the two vertices are adjacent in the world
            if world[i] == 1 and world[j] == 1:
                # Increment the number of edges
                edges += 1
    
    # Check if the minimum cut of the world is at least m
    return edges >= m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_number_of_non_similar_worlds(n, m))

