
def get_boring_pairs(paths):
    # Initialize a set to store the boring pairs
    boring_pairs = set()
    
    # Iterate over the paths
    for path in paths:
        # Get the planets and curiosity of the path
        planets = path[0:2]
        curiosity = path[2]
        
        # Check if the planets are different
        if planets[0] != planets[1]:
            # Add the planets to the boring pairs set if the XOR of the curiosity is 0
            if curiosity == 0:
                boring_pairs.add(tuple(sorted(planets)))
    
    # Return the boring pairs set
    return boring_pairs

def get_boring_pairs_after_k_destructions(paths, k):
    # Get the boring pairs before the first destruction
    boring_pairs = get_boring_pairs(paths[:k])
    
    # Iterate over the remaining paths
    for path in paths[k:]:
        # Get the planets and curiosity of the path
        planets = path[0:2]
        curiosity = path[2]
        
        # Check if the planets are different
        if planets[0] != planets[1]:
            # Remove the planets from the boring pairs set if the XOR of the curiosity is not 0
            if curiosity != 0:
                boring_pairs.discard(tuple(sorted(planets)))
    
    # Return the number of boring pairs after the destruction
    return len(boring_pairs)

if __name__ == '__main__':
    # Get the input
    num_planets = int(input())
    paths = []
    for _ in range(num_planets - 1):
        path = list(map(int, input().split()))
        paths.append(path)
    permutation = list(map(int, input().split()))
    
    # Initialize the number of boring pairs before the first destruction
    num_boring_pairs = len(get_boring_pairs(paths))
    
    # Iterate over the permutation
    for i in range(num_planets - 1):
        # Get the planets and curiosity of the path
        planets = paths[permutation[i] - 1][0:2]
        curiosity = paths[permutation[i] - 1][2]
        
        # Check if the planets are different
        if planets[0] != planets[1]:
            # Remove the planets from the boring pairs set if the XOR of the curiosity is not 0
            if curiosity != 0:
                num_boring_pairs -= 1
        
        # Print the number of boring pairs after the destruction
        print(num_boring_pairs)

