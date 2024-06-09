
def solve(n, g, stations):
    # Sort the stations by distance
    stations = sorted(stations, key=lambda x: x[0])
    
    # Initialize the current gas tank with the full capacity
    curr_tank = g
    
    # Initialize the total cost to 0
    total_cost = 0
    
    # Iterate through the stations
    for i in range(n):
        # Calculate the distance to the next station
        dist = stations[i][0] - stations[i-1][0] if i > 0 else stations[i][0]
        
        # Calculate the cost to refuel at the current station
        cost = dist // curr_tank * stations[i][1]
        
        # Update the current gas tank
        curr_tank = g - dist % curr_tank
        
        # If the current gas tank is negative, it means we will run out of gas
        if curr_tank < 0:
            return "cancel road trip"
        
        # Add the cost to the total cost
        total_cost += cost
    
    # Return the total cost
    return total_cost

