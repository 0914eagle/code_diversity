
def solve(n, g, dist, cost):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    curr_capacity = 0
    # Initialize the current distance traveled as 0
    curr_dist = 0
    # Sort the gas stations by distance in ascending order
    sorted_stations = sorted(zip(dist, cost), key=lambda x: x[0])
    # Iterate through the gas stations
    for station in sorted_stations:
        # Calculate the distance to the current gas station
        dist_to_station = station[0] - curr_dist
        # Calculate the cost to travel to the current gas station
        travel_cost = dist_to_station * station[1]
        # Check if the current gas tank capacity is enough to travel to the current gas station
        if curr_capacity >= dist_to_station:
            # Update the current distance traveled
            curr_dist = station[0]
            # Update the current gas tank capacity
            curr_capacity -= dist_to_station
        else:
            # Calculate the amount of gas needed to travel to the current gas station
            gas_needed = dist_to_station - curr_capacity
            # Check if the gas needed is more than the current gas tank capacity
            if gas_needed > g:
                # Return "cancel road trip" if the gas needed is more than the current gas tank capacity
                return "cancel road trip"
            # Update the current distance traveled
            curr_dist = station[0]
            # Update the current gas tank capacity
            curr_capacity = g - gas_needed
        # Update the minimum cost to travel to the rightmost gas station
        min_cost = min(min_cost, travel_cost)
    # Return the minimum cost to travel to the rightmost gas station
    return min_cost

