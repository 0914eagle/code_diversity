
def solve(cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities.sort()
    towers.sort()
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the first city that is not covered by any tower
    for i in range(len(cities)):
        if cities[i] - towers[0] > min_dist:
            # If the city is not covered by the first tower, find the next tower that covers the city
            for j in range(1, len(towers)):
                if cities[i] - towers[j] <= min_dist:
                    # Update the minimum distance to the distance between the city and the tower
                    min_dist = cities[i] - towers[j]
                    break
    
    # Return the minimum distance
    return min_dist
