
def solve(n, g, dist, cost):
    # Sort the gas stations by distance in ascending order
    sorted_stations = sorted(zip(dist, cost), key=lambda x: x[0])

    # Initialize the current distance and cost
    current_dist = 0
    current_cost = 0

    # Loop through the gas stations
    for i in range(n):
        # Calculate the distance to the next gas station
        next_dist = sorted_stations[i][0] - current_dist

        # Calculate the cost to reach the next gas station
        next_cost = sorted_stations[i][1] * next_dist

        # Check if the next gas station is within the fuel tank capacity
        if next_dist <= g:
            # Fuel up at the next gas station
            current_dist = sorted_stations[i][0]
            current_cost += next_cost
        else:
            # Cancel the road trip if the next gas station is out of range
            return "cancel road trip"

    # Return the minimum cost to complete the trip
    return current_cost

