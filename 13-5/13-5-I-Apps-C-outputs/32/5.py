
def longest_path(n, m, roads):
    # Initialize a dictionary to store the lengths of the paths
    paths = {}
    
    # Iterate over each road
    for road in roads:
        # Get the two cities connected by the road
        city1, city2 = road
        
        # If the path starting from city1 and ending in city2 is not in the dictionary, add it to the dictionary with length 1
        if (city1, city2) not in paths:
            paths[(city1, city2)] = 1
        
        # If the path starting from city2 and ending in city1 is not in the dictionary, add it to the dictionary with length 1
        if (city2, city1) not in paths:
            paths[(city2, city1)] = 1
        
        # If the path starting from city1 and ending in city2 is already in the dictionary, increase its length by 1
        if (city1, city2) in paths:
            paths[(city1, city2)] += 1
        
        # If the path starting from city2 and ending in city1 is already in the dictionary, increase its length by 1
        if (city2, city1) in paths:
            paths[(city2, city1)] += 1
    
    # Find the longest path in the dictionary
    longest_path = max(paths.values())
    
    return longest_path

