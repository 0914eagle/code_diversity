
def solve(n, g, distances, costs):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current gas station and the total cost
    current_gas_station = 0
    total_cost = 0

    # Loop through each gas station
    for i in range(n):
        # Calculate the distance to the next gas station
        distance_to_next_gas_station = sorted_gas_stations[i][0] - sorted_gas_stations[current_gas_station][0]

        # Calculate the cost to travel to the next gas station
        travel_cost = distance_to_next_gas_station * sorted_gas_stations[current_gas_station][1]

        # Check if the total cost plus the travel cost is less than or equal to the tank capacity
        if total_cost + travel_cost <= g:
            # Add the travel cost to the total cost
            total_cost += travel_cost

            # Update the current gas station
            current_gas_station = i
        else:
            # If the total cost plus the travel cost is greater than the tank capacity, cancel the road trip
            return "cancel road trip"

    # If the loop completes successfully, return the total cost
    return total_cost

