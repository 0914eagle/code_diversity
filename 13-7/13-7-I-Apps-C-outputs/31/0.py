
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
        
        # Check if the next station is within reach
        if next_dist <= g:
            # Calculate the amount of gas needed for the next station
            needed_gas = next_dist - curr_dist
            
            # Add the cost of the needed gas to the total cost
            curr_cost += needed_gas * station[1]
            
            # Update the current distance and fuel level
            curr_dist = station[0]
        else:
            # If the next station is out of reach, cancel the trip
            return "cancel road trip"
    
    # Return the total cost if the trip is possible
    return curr_cost

