
def get_boring_pairs(planets, paths):
    # Initialize a set to store the boring pairs
    boring_pairs = set()
    
    # Iterate over each path
    for path in paths:
        # Get the two planets connected by the path
        planet_a, planet_b = path[0], path[1]
        
        # If the two planets are not the same
        if planet_a != planet_b:
            # Add the boring pair to the set
            boring_pairs.add((planet_a, planet_b))
    
    # Return the set of boring pairs
    return boring_pairs

def get_destroyed_boring_pairs(planets, paths, destroyed_paths):
    # Get the set of boring pairs before destruction
    boring_pairs = get_boring_pairs(planets, paths)
    
    # Initialize a set to store the destroyed boring pairs
    destroyed_boring_pairs = set()
    
    # Iterate over the destroyed paths
    for path in destroyed_paths:
        # Get the two planets connected by the path
        planet_a, planet_b = path[0], path[1]
        
        # If the two planets are not the same
        if planet_a != planet_b:
            # Add the destroyed boring pair to the set
            destroyed_boring_pairs.add((planet_a, planet_b))
    
    # Return the set of destroyed boring pairs
    return destroyed_boring_pairs

def main():
    # Read the number of planets and paths
    num_planets, num_paths = map(int, input().split())
    
    # Read the paths
    paths = []
    for _ in range(num_paths):
        paths.append(list(map(int, input().split())))
    
    # Read the destroyed paths
    destroyed_paths = list(map(int, input().split()))
    
    # Get the set of boring pairs before destruction
    boring_pairs = get_boring_pairs(num_planets, paths)
    
    # Get the set of destroyed boring pairs
    destroyed_boring_pairs = get_destroyed_boring_pairs(num_planets, paths, destroyed_paths)
    
    # Iterate over the destroyed paths
    for i in range(len(destroyed_paths)):
        # Get the destroyed path
        destroyed_path = destroyed_paths[i]
        
        # Get the two planets connected by the destroyed path
        planet_a, planet_b = paths[destroyed_path - 1][0], paths[destroyed_path - 1][1]
        
        # If the two planets are not the same
        if planet_a != planet_b:
            # Remove the destroyed boring pair from the set
            boring_pairs.remove((planet_a, planet_b))
    
    # Print the number of boring pairs after each destruction
    for i in range(len(destroyed_paths)):
        print(len(boring_pairs))

if __name__ == '__main__':
    main()

