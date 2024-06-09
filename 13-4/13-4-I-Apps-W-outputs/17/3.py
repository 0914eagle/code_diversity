
def solve(cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities.sort()
    towers.sort()
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and towers
    for city, tower in zip(cities, towers):
        # If the city is not covered by the current tower, increase the minimum distance
        if city > tower:
            min_dist += 1
    
    return min_dist

