
def solve(cities, towers):
    # Sort the cities and towers by their x-coordinates
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum radius as 0
    r = 0
    
    # Iterate through the cities and find the closest tower
    for i in range(len(cities)):
        # Find the closest tower to the current city
        for j in range(len(towers)):
            if cities[i] - towers[j] <= r:
                break
        else:
            # If no tower is found, increase the radius by 1 and try again
            r += 1
            continue
    
    return r

