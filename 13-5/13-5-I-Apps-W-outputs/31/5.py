
def solve(cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the first city that is not covered by any tower
    for i in range(len(cities)):
        if cities[i] > towers[-1]:
            # If the city is not covered by any tower, return the minimum distance as the maximum distance between the city and the last tower
            return cities[i] - towers[-1]
        elif cities[i] < towers[0]:
            # If the city is covered by the first tower, set the minimum distance as the distance between the city and the first tower
            min_dist = cities[i] - towers[0]
    
    # If all cities are covered by towers, return the minimum distance
    return min_dist

