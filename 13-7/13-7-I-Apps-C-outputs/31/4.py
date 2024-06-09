
def get_min_cost(distances, costs, gas_tank):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current distance, fuel in tank, and total cost
    current_distance = 0
    fuel_in_tank = 0
    total_cost = 0

    # Loop through each gas station
    for distance, cost in sorted_gas_stations:
        # Calculate the distance from the current position to the next gas station
        next_distance = distance - current_distance

        # Check if the fuel in tank is enough to travel to the next gas station
        if next_distance <= fuel_in_tank:
            # Consume the fuel and update the current distance and fuel in tank
            fuel_in_tank -= next_distance
            current_distance = distance
        else:
            # Calculate the amount of fuel needed to travel to the next gas station
            fuel_needed = next_distance - fuel_in_tank

            # Check if the fuel needed is more than the gas tank capacity
            if fuel_needed > gas_tank:
                return "cancel road trip"

            # Fill up the gas tank, update the fuel in tank, and add the cost to the total cost
            fuel_in_tank = gas_tank
            total_cost += fuel_needed * cost
            current_distance = distance

    # Return the total cost
    return total_cost

