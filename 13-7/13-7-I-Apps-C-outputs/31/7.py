
def solve(n, g, dist, cost):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(dist, cost), key=lambda x: x[0])

    # Initialize the current gas station and the total distance traveled
    current_gas_station = 0
    total_distance = 0

    # Initialize the minimum cost to travel to the rightmost gas station
    min_cost = 0

    # Loop through each gas station
    for i in range(n):
        # Calculate the distance from the current gas station to the next gas station
        distance_to_next_gas_station = sorted_gas_stations[i][0] - total_distance

        # Calculate the amount of gas needed to travel to the next gas station
        gas_needed = distance_to_next_gas_station // 1000

        # Check if the gas needed is less than or equal to the gas tank capacity
        if gas_needed <= g:
            # Calculate the cost of traveling to the next gas station
            cost_to_next_gas_station = sorted_gas_stations[i][1] * gas_needed

            # Update the minimum cost to travel to the rightmost gas station
            min_cost += cost_to_next_gas_station

            # Update the current gas station and the total distance traveled
            current_gas_station = i
            total_distance += distance_to_next_gas_station

        # If the gas needed is greater than the gas tank capacity, cancel the road trip
        else:
            return "cancel road trip"

    # If the road trip is not canceled, return the minimum cost to travel to the rightmost gas station
    return min_cost

