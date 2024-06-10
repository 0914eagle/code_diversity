
def get_good_observatories(elevations, roads):
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    # Iterate over each observatory and its elevation
    for observatory, elevation in enumerate(elevations):
        # Initialize a set to store the observatories that can be reached from the current observatory using just one road
        reachable_observatories = set()
        
        # Iterate over each road
        for road in roads:
            # If the current observatory is one of the endpoints of the road
            if observatory in road:
                # Add the other endpoint of the road to the set of reachable observatories
                reachable_observatories.add(road[0] if road[1] == observatory else road[1])
        
        # If the current observatory is not in the set of reachable observatories or if its elevation is higher than that of all reachable observatories
        if observatory not in reachable_observatories or elevation > max(elevations[i] for i in reachable_observatories):
            # Add the current observatory to the set of good observatories
            good_observatories.add(observatory)
    
    # Return the number of good observatories
    return len(good_observatories)

def main():
    # Read the number of observatories and roads from stdin
    num_observatories, num_roads = map(int, input().split())
    
    # Read the elevations of the observatories from stdin
    elevations = list(map(int, input().split()))
    
    # Read the roads from stdin
    roads = [tuple(map(int, input().split())) for _ in range(num_roads)]
    
    # Call the get_good_observatories function and print the result
    print(get_good_observatories(elevations, roads))

if __name__ == '__main__':
    main()

