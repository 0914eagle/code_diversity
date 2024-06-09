
def longest_race_path(N, M, roads):
    # Initialize a dictionary to store the longest path from each city
    longest_paths = {}
    for i in range(1, N+1):
        longest_paths[i] = 0
    
    # Iterate over the roads
    for road in roads:
        city1, city2 = road[0], road[1]
        if longest_paths[city1] < longest_paths[city2] + 1:
            longest_paths[city1] = longest_paths[city2] + 1
    
    # Return the longest path from city 1
    return longest_paths[1]

