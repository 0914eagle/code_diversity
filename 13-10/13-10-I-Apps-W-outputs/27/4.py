
def get_boring_pairs(planets, paths):
    # Initialize a set to store the boring pairs
    boring_pairs = set()
    
    # Iterate over each path
    for path in paths:
        # Get the two planets connected by the path
        planet_a, planet_b = path[0], path[1]
        
        # Check if the XOR of the path curiosity is equal to 0
        if xor_curiosity(path) == 0:
            # Add the pair of planets to the boring pairs set
            boring_pairs.add((planet_a, planet_b))
    
    return boring_pairs

def xor_curiosity(path):
    # Get the curiosity of the path
    curiosity = path[2]
    
    # Return the XOR of the curiosity
    return curiosity ^ 0

def get_num_boring_pairs(planets, paths, destroyed_paths):
    # Get the boring pairs before any path is destroyed
    before_destroyed = get_boring_pairs(planets, paths)
    
    # Iterate over each destroyed path
    for destroyed_path in destroyed_paths:
        # Get the two planets connected by the destroyed path
        planet_a, planet_b = destroyed_path[0], destroyed_path[1]
        
        # Check if the destroyed path is in the boring pairs set
        if (planet_a, planet_b) in before_destroyed:
            # Remove the pair of planets from the boring pairs set
            before_destroyed.remove((planet_a, planet_b))
    
    # Return the number of boring pairs after each destruction
    return len(before_destroyed)

def main():
    # Read the number of planets and paths
    num_planets, num_paths = map(int, input().split())
    
    # Read the planets and paths
    planets = set(map(int, input().split()))
    paths = []
    for _ in range(num_paths):
        paths.append(list(map(int, input().split())))
    
    # Read the destroyed paths order
    destroyed_paths = list(map(int, input().split()))
    
    # Get the number of boring pairs after each destruction
    num_boring_pairs = get_num_boring_pairs(planets, paths, destroyed_paths)
    
    # Print the number of boring pairs after each destruction
    for i in range(num_paths):
        print(num_boring_pairs[i])

if __name__ == '__main__':
    main()

