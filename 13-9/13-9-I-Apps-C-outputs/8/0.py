
def solve_road_trip(n, g, distances, costs):
    # Sort the gas stations by distance
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current distance and cost
    current_distance = 0
    current_cost = 0

    # Loop through each gas station
    for distance, cost in sorted_gas_stations:
        # Calculate the distance to the next gas station
        next_distance = distance - current_distance

        # Check if the next gas station is within reach
        if next_distance <= g:
            # Fuel up and update the current distance and cost
            current_cost += cost * (next_distance / 1000)
            current_distance = distance
        else:
            # Cancel the road trip
            return "cancel road trip"

    # Return the minimum cost
    return current_cost

