
def longest_path(N, M, roads):
    # Initialize a dictionary to store the length of the longest path from each city
    longest_paths = {}
    for i in range(1, N+1):
        longest_paths[i] = 0
    
    # Initialize a dictionary to store the previous city in the longest path from each city
    previous_cities = {}
    for i in range(1, N+1):
        previous_cities[i] = 0
    
    # Iterate over the roads
    for road in roads:
        city1, city2 = road[0], road[1]
        if longest_paths[city1] >= longest_paths[city2]:
            longest_paths[city2] = longest_paths[city1] + 1
            previous_cities[city2] = city1
        else:
            longest_paths[city1] = longest_paths[city2] + 1
            previous_cities[city1] = city2
    
    # Find the longest path that ends in city 1
    max_length = 0
    current_city = 1
    while current_city != 0:
        max_length = max(max_length, longest_paths[current_city])
        current_city = previous_cities[current_city]
    
    return max_length

