
def solve(n, g, dist, cost):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(dist, cost), key=lambda x: x[0])

    # Initialize the current distance and cost
    current_distance = 0
    current_cost = 0

    # Loop through each gas station
    for i in range(n):
        # Calculate the distance to the next gas station
        next_distance = sorted_gas_stations[i][0] - current_distance

        # Check if the next gas station is within reach
        if next_distance <= g:
            # Fuel up at the next gas station
            current_cost += sorted_gas_stations[i][1]
            current_distance = sorted_gas_stations[i][0]
        else:
            # Cancel the road trip
            return "cancel road trip"

    # Return the total cost of the trip
    return current_cost

