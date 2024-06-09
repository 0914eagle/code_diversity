
def solve(n, x, y, c, k):
    # Convert input to a list of cities and their coordinates
    cities = [(x[i], y[i]) for i in range(n)]
    
    # Initialize the minimum cost and the set of cities with power stations
    min_cost = 0
    power_stations = set()
    
    # Loop through each city and calculate the cost of connecting it to the nearest power station
    for i in range(n):
        # If the city has not been assigned a power station, calculate the cost of connecting it to the nearest power station
        if i not in power_stations:
            # Find the nearest power station to the current city
            nearest_power_station = min(power_stations, key=lambda x: abs(x[0] - cities[i][0]) + abs(x[1] - cities[i][1]))
            
            # Calculate the cost of connecting the current city to the nearest power station
            cost = k[i] + k[nearest_power_station[1]] + abs(cities[i][0] - nearest_power_station[0]) + abs(cities[i][1] - nearest_power_station[1])
            
            # If the cost is less than the minimum cost, update the minimum cost and the set of power stations
            if cost < min_cost:
                min_cost = cost
                power_stations = set([i])
        
        # If the city has already been assigned a power station, add it to the set of power stations
        else:
            power_stations.add(i)
    
    # Return the minimum cost and the set of power stations
    return min_cost, power_stations

