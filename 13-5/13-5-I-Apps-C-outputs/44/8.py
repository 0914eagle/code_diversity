
def solve(n, g, dist, cost):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(dist, cost), key=lambda x: x[0])

    # Initialize the current distance and cost variables
    current_distance = 0
    current_cost = 0

    # Loop through each gas station
    for i in range(n):
        # Calculate the distance to the next gas station
        next_distance = sorted_gas_stations[i][0] - current_distance

        # Calculate the cost to reach the next gas station
        next_cost = sorted_gas_stations[i][1] * (next_distance // 1000)

        # Check if the next gas station is within the fuel tank capacity
        if next_distance + current_distance <= g:
            # Add the cost to reach the next gas station to the total cost
            current_cost += next_cost

            # Update the current distance
            current_distance = sorted_gas_stations[i][0]
        else:
            # If the next gas station is not within the fuel tank capacity, cancel the road trip
            return "cancel road trip"

    # If the trip is possible, return the minimum cost
    return current_cost

