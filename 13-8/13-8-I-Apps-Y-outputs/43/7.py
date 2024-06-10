
def get_good_observatories(num_observatories, num_roads, observatory_elevations, road_connections):
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    # Loop through each observatory
    for observatory in range(num_observatories):
        # Check if the observatory is already in the good observatories set
        if observatory not in good_observatories:
            # Initialize a set to store the observatories that can be reached from the current observatory using just one road
            reachable_observatories = set()
            
            # Loop through each road
            for road in range(num_roads):
                # Check if the current road connects the current observatory to another observatory
                if road_connections[road][0] == observatory or road_connections[road][1] == observatory:
                    # Add the other observatory to the reachable observatories set
                    reachable_observatories.add(road_connections[road][0] if road_connections[road][1] == observatory else road_connections[road][1])
            
            # Check if the current observatory has a higher elevation than all the observatories it can reach from using just one road
            if observatory_elevations[observatory] > max(observatory_elevations[reachable_observatory] for reachable_observatory in reachable_observatories):
                # Add the current observatory to the good observatories set
                good_observatories.add(observatory)
    
    # Return the number of good observatories
    return len(good_observatories)

def main():
    # Read the number of observatories and roads
    num_observatories, num_roads = map(int, input().split())
    
    # Read the elevations of the observatories
    observatory_elevations = list(map(int, input().split()))
    
    # Read the connections between the roads
    road_connections = []
    for _ in range(num_roads):
        road_connections.append(list(map(int, input().split())))
    
    # Call the get_good_observatories function and print the result
    print(get_good_observatories(num_observatories, num_roads, observatory_elevations, road_connections))

if __name__ == '__main__':
    main()

