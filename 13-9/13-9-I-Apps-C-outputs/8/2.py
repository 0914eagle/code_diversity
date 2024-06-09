
def solve(n, g, distances, costs):
    # Sort the gas stations by distance
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current position and fuel level
    current_position = 0
    fuel_level = g

    # Initialize the minimum cost
    min_cost = 0

    # Iterate through the sorted gas stations
    for i in range(n):
        # Get the distance and cost of the current gas station
        distance, cost = sorted_gas_stations[i]

        # Check if the current gas station is within reach
        if current_position + distance <= fuel_level:
            # Fuel up and update the fuel level
            fuel_level -= distance
            min_cost += cost
        else:
            # Cancel the road trip
            return "cancel road trip"

    # Return the minimum cost
    return min_cost

