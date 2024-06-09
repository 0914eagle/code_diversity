
def get_min_cost(distances, costs, tank_capacity):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current distance and cost
    current_distance = 0
    current_cost = 0

    # Loop through each gas station
    for i in range(len(sorted_gas_stations)):
        # Calculate the distance to the next gas station
        next_distance = sorted_gas_stations[i][0] - current_distance

        # Check if the next gas station is within driving distance
        if next_distance <= tank_capacity:
            # Add the cost of the next gas station to the total cost
            current_cost += sorted_gas_stations[i][1]

            # Update the current distance
            current_distance = sorted_gas_stations[i][0]
        else:
            # Calculate the distance that can be traveled with the current tank capacity
            traveled_distance = tank_capacity

            # Calculate the cost of the traveled distance
            traveled_cost = current_cost + (traveled_distance / next_distance) * sorted_gas_stations[i][1]

            # Check if the traveled cost is less than the total cost
            if traveled_cost < current_cost:
                # Update the current cost and distance
                current_cost = traveled_cost
                current_distance = traveled_distance
            else:
                # Return the current cost
                return current_cost

    # Return the final cost
    return current_cost

