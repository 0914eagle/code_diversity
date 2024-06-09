
import sys

def shortest_paths(n, roads):
    # Initialize a dictionary to store the number of shortest paths for each road
    num_shortest_paths = {}
    
    # Loop through each road
    for road in roads:
        # Get the origin and destination cities and the length of the road
        origin, destination, length = road
        
        # If the road is not already in the dictionary, add it with a count of 1
        if road not in num_shortest_paths:
            num_shortest_paths[road] = 1
        
        # Loop through all the other roads
        for other_road in roads:
            # If the other road is not the same as the current road
            if other_road != road:
                # Get the origin and destination cities and the length of the other road
                other_origin, other_destination, other_length = other_road
                
                # If the other road is a continuation of the current road
                if other_origin == destination:
                    # Increment the count of shortest paths for the current road
                    num_shortest_paths[road] += 1
    
    # Return the number of shortest paths for each road
    return num_shortest_paths

n, m = map(int, input().split())
roads = []
for _ in range(m):
    origin, destination, length = map(int, input().split())
    roads.append((origin, destination, length))

num_shortest_paths = shortest_paths(n, roads)

for road in roads:
    print(num_shortest_paths[road] % 1000000007)


