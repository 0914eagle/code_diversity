
def get_min_cost(distances, costs, tank_capacity):
    # Sort the gas stations by distance
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current distance, cost, and fuel left
    current_distance = 0
    current_cost = 0
    fuel_left = tank_capacity

    # Loop through the gas stations
    for distance, cost in sorted_gas_stations:
        # Calculate the distance to the next gas station
        next_distance = distance - current_distance

        # Check if the fuel left is enough to reach the next gas station
        if next_distance <= fuel_left:
            # Add the cost of the gas to the current cost
            current_cost += cost * (next_distance / 1000)

            # Subtract the fuel used from the fuel left
            fuel_left -= next_distance

            # Update the current distance
            current_distance = distance
        else:
            # Calculate the distance the car can travel with the current fuel
            travel_distance = fuel_left / 1000

            # Add the cost of the gas to the current cost
            current_cost += cost * travel_distance

            # Update the fuel left
            fuel_left = 0

            # Break out of the loop
            break

    # Check if the car has enough fuel to reach the final destination
    if fuel_left == 0:
        return current_cost
    else:
        return "cancel road trip"

