
def min_cost_to_travel(gas_stations, fuel_tank_capacity):
    # Sort the gas stations by distance from left to right
    gas_stations.sort(key=lambda x: x[0])
    
    # Initialize the current distance from the origin to 0
    current_distance = 0
    
    # Initialize the current fuel level to the fuel tank capacity
    current_fuel_level = fuel_tank_capacity
    
    # Initialize the minimum cost to travel to the rightmost gas station to infinity
    min_cost = float('inf')
    
    # Iterate through the gas stations
    for gas_station in gas_stations:
        # Calculate the distance from the current position to the gas station
        distance_to_gas_station = gas_station[0] - current_distance
        
        # Calculate the fuel needed to reach the gas station
        fuel_needed = distance_to_gas_station / 1000
        
        # If the fuel needed is less than or equal to the current fuel level, fill up the tank and update the current fuel level
        if fuel_needed <= current_fuel_level:
            current_fuel_level = fuel_tank_capacity
        # Otherwise, calculate the fuel needed to travel the remaining distance and update the current fuel level
        else:
            current_fuel_level -= fuel_needed - current_fuel_level
        
        # Add the cost of gas at the current gas station to the minimum cost
        min_cost += gas_station[1]
        
        # Update the current distance to the gas station
        current_distance = gas_station[0]
    
    # If the current fuel level is non-negative, return the minimum cost
    if current_fuel_level >= 0:
        return min_cost
    # Otherwise, return "cancel road trip"
    else:
        return "cancel road trip"

