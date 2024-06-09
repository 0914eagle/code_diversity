
def solve(cities, towers):
    # Sort the cities and towers by their x-coordinates
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the first city that is not covered by any tower
    for i in range(len(cities)):
        if cities[i] > towers[-1]:
            # If the city is not covered by any tower, return the minimum distance
            return min_dist
        else:
            # Otherwise, find the closest tower to the city and update the minimum distance
            for j in range(len(towers)):
                if cities[i] <= towers[j]:
                    min_dist = max(min_dist, cities[i] - towers[j])
                    break
    
    # If all cities are covered by towers, return the minimum distance
    return min_dist

