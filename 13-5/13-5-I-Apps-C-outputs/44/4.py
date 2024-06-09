
def solve(n, g, stations):
    # Sort the stations by distance
    stations = sorted(stations, key=lambda x: x[0])
    
    # Initialize the current distance and cost
    curr_dist = 0
    curr_cost = 0
    
    # Loop through each station
    for station in stations:
        # Calculate the distance to the next station
        next_dist = station[0] - curr_dist
        
        # Calculate the amount of gas needed for the trip to the next station
        needed_gas = next_dist / 1000
        
        # Check if the needed gas is less than or equal to the tank capacity
        if needed_gas <= g:
            # Add the cost of the gas to the current cost
            curr_cost += needed_gas * station[1]
            
            # Update the current distance
            curr_dist = station[0]
        else:
            # If the needed gas is greater than the tank capacity, return "cancel road trip"
            return "cancel road trip"
    
    # Return the final cost
    return curr_cost

