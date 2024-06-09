
def longest_race_path(N, M, roads):
    # Initialize a dictionary to store the lengths of the simple paths
    simple_paths = {}
    
    # Iterate over each road
    for road in roads:
        # Get the cities connected by the road
        city1, city2 = road
        
        # If the path starting from city1 and ending in city2 is not in the dictionary, add it to the dictionary with length 1
        if (city1, city2) not in simple_paths:
            simple_paths[(city1, city2)] = 1
        
        # If the path starting from city2 and ending in city1 is not in the dictionary, add it to the dictionary with length 1
        if (city2, city1) not in simple_paths:
            simple_paths[(city2, city1)] = 1
    
    # Initialize the longest path length to 0
    longest_path_length = 0
    
    # Iterate over each city
    for city in range(1, N+1):
        # Initialize a set to store the cities visited in the current path
        visited_cities = set()
        
        # Initialize the current city as the starting city
        current_city = city
        
        # Initialize the current path length to 0
        current_path_length = 0
        
        # While the current city is not the starting city or the path length is greater than the longest path length, iterate over the simple paths
        while current_city != city or current_path_length > longest_path_length:
            # If the current city is not in the visited cities set, add it to the set and increment the current path length
            if current_city not in visited_cities:
                visited_cities.add(current_city)
                current_path_length += 1
            
            # Get the next city in the path by looking up the simple path in the dictionary
            next_city = simple_paths[(current_city, city)]
            
            # Update the current city to the next city
            current_city = next_city
        
        # If the current path length is greater than the longest path length, update the longest path length
        if current_path_length > longest_path_length:
            longest_path_length = current_path_length
    
    # Return the longest path length
    return longest_path_length

