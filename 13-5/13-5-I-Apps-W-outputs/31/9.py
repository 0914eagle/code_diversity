
def solve(n, m, cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Loop through each city and tower
    for city, tower in zip(cities, towers):
        # If the city is not covered by the current tower, find the next tower that covers it
        if city > tower:
            min_dist = max(min_dist, city - tower)
    
    # Return the minimum distance
    return min_dist

