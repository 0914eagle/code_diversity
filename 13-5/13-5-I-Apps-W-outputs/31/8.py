
def solve(cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities.sort()
    towers.sort()
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the first city that is not covered by any tower
    for i in range(len(cities)):
        if cities[i] > towers[-1]:
            # If the city is not covered by any tower, return the minimum distance
            return min_dist
        else:
            # Otherwise, find the closest tower to the city
            for j in range(len(towers)):
                if cities[i] <= towers[j]:
                    # If the city is covered by the tower, break the loop
                    break
            # Update the minimum distance to the distance between the city and the tower
            min_dist = max(min_dist, abs(cities[i] - towers[j]))
    
    # If all cities are covered by towers, return the minimum distance
    return min_dist

