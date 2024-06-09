
def solve(n, g, d, c):
    # Sort the gas stations by distance
    sorted_gas_stations = sorted(zip(d, c), key=lambda x: x[0])

    # Initialize the current gas tank with the full capacity
    current_gas_tank = g

    # Initialize the total cost to 0
    total_cost = 0

    # Iterate through the sorted gas stations
    for i in range(n):
        # Calculate the distance to the next gas station
        distance_to_next_gas_station = sorted_gas_stations[i][0]

        # Calculate the cost to reach the next gas station
        cost_to_next_gas_station = sorted_gas_stations[i][1]

        # Calculate the amount of gas needed to reach the next gas station
        gas_needed = distance_to_next_gas_station - current_gas_tank

        # If the gas needed is negative, it means we have enough gas to reach the next gas station
        if gas_needed <= 0:
            # Add the cost of the current gas station to the total cost
            total_cost += cost_to_next_gas_station

            # Subtract the gas needed from the current gas tank
            current_gas_tank -= gas_needed

        # If the gas needed is positive, it means we don't have enough gas to reach the next gas station
        else:
            # Calculate the amount of gas we can buy at the current gas station
            gas_available = current_gas_tank * cost_to_next_gas_station

            # If the gas available is less than the gas needed, it means we can't reach the next gas station
            if gas_available < gas_needed:
                return "cancel road trip"

            # Add the cost of the current gas station to the total cost
            total_cost += gas_available

            # Fill the gas tank with the amount of gas available
            current_gas_tank = gas_available / cost_to_next_gas_station

    # If we reach the end of the list of gas stations, it means we have enough gas to reach the destination
    return total_cost

