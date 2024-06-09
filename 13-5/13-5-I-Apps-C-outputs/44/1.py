
def get_min_cost(distances, costs, tank_capacity):
    # Sort the gas stations by distance
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current distance, fuel, and cost
    current_distance = 0
    fuel = tank_capacity
    cost = 0

    # Loop through the gas stations
    for distance, cost_per_gallon in sorted_gas_stations:
        # Calculate the fuel needed for this gas station
        fuel_needed = distance - current_distance

        # Check if the fuel needed is greater than the fuel in the tank
        if fuel_needed > fuel:
            return "cancel road trip"

        # Calculate the fuel available after refueling
        fuel_available = tank_capacity - fuel

        # Calculate the number of gallons needed for this gas station
        num_gallons = fuel_needed // fuel_available

        # Calculate the cost for this gas station
        cost += num_gallons * cost_per_gallon

        # Update the current distance and fuel
        current_distance = distance
        fuel = tank_capacity - (fuel_needed % fuel_available)

    return cost

