
def longest_race_path(N, M, roads):
    # Initialize a dictionary to store the longest path from each city
    longest_paths = {}
    for i in range(1, N+1):
        longest_paths[i] = 0
    
    # Initialize a dictionary to store the previous city in the path for each city
    previous_cities = {}
    for i in range(1, N+1):
        previous_cities[i] = -1
    
    # Loop through each road
    for road in roads:
        # Get the two cities connected by the road
        city1, city2 = road
        
        # If the longest path from city1 is greater than the longest path from city2 to city1 plus the length of the road, update the longest path and previous city
        if longest_paths[city1] > longest_paths[city2] + 1:
            longest_paths[city2] = longest_paths[city1] + 1
            previous_cities[city2] = city1
        # If the longest path from city2 is greater than the longest path from city1 to city2 plus the length of the road, update the longest path and previous city
        elif longest_paths[city2] > longest_paths[city1] + 1:
            longest_paths[city1] = longest_paths[city2] + 1
            previous_cities[city1] = city2
    
    # Return the longest path from city 1 to city N
    return longest_paths[N]

