
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

        # Calculate the cost to reach the next gas station
        next_cost = sorted_gas_stations[i][1] * (next_distance // 1)

        # Check if the trip is possible with the current gas tank capacity
        if current_cost + next_cost > g:
            return "cancel road trip"

        # Fill up the gas tank at the current gas station
        current_cost += next_cost

        # Update the current distance and cost
        current_distance = sorted_gas_stations[i][0]

    # Return the minimum cost to complete the trip
    return current_cost

