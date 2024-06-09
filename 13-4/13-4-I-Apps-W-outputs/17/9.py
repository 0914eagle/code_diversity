
def solve(cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities.sort()
    towers.sort()
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the first city that is not covered by any tower
    for i in range(len(cities)):
        if cities[i] - towers[0] > min_dist:
            # If the city is not covered by any tower, find the closest tower and update the minimum distance
            for j in range(len(towers)):
                if cities[i] - towers[j] <= min_dist:
                    min_dist = cities[i] - towers[j]
                    break
    
    return min_dist

