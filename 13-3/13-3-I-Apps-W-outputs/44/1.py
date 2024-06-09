
def solve(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the shortest distance from each section to the destination
    distances = {}
    
    # Loop through each query
    for query in queries:
        # Initialize the shortest distance to the maximum possible value
        shortest_distance = float('inf')
        
        # Loop through each section on the current floor
        for section in range(1, m+1):
            # If the section is not occupied by a stair or elevator
            if section not in stairs and section not in elevators:
                # Calculate the distance to the destination from this section
                distance = abs(query[0] - section) + abs(query[1] - section)
                
                # If the distance is shorter than the current shortest distance, update the shortest distance
                if distance < shortest_distance:
                    shortest_distance = distance
        
        # Add the shortest distance to the dictionary
        distances[query] = shortest_distance
    
    # Return the dictionary of shortest distances
    return distances

