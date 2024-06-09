
def solve(n, g, stations):
    # Sort the stations by distance
    stations = sorted(stations, key=lambda x: x[0])
    
    # Initialize the current fuel and cost
    fuel = g
    cost = 0
    
    # Loop through the stations
    for i in range(n):
        # Calculate the distance to the next station
        distance = stations[i][0] - stations[i-1][0] if i > 0 else stations[i][0]
        
        # Calculate the fuel needed for the next station
        needed = distance - fuel
        
        # Check if the next station is within reach
        if needed <= 0:
            # Fuel up and continue
            fuel += needed
            cost += needed * stations[i][1]
        else:
            # Cannot reach the next station, cancel the trip
            return "cancel road trip"
    
    # Return the minimum cost
    return cost

