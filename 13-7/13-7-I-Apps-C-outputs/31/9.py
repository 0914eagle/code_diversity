
def get_min_cost(distances, costs, tank_capacity):
    # Sort the distances and costs in ascending order
    sorted_distances = sorted(distances)
    sorted_costs = sorted(costs)
    
    # Initialize the minimum cost and the current fuel level
    min_cost = 0
    fuel_level = tank_capacity
    
    # Loop through the distances and costs
    for i in range(len(sorted_distances)):
        # Calculate the distance to the next gas station
        distance = sorted_distances[i]
        
        # Calculate the cost of fuel needed for the next gas station
        fuel_needed = distance - fuel_level
        if fuel_needed > 0:
            # Calculate the cost of fuel for the next gas station
            fuel_cost = fuel_needed * sorted_costs[i]
            
            # Check if the fuel cost is less than the tank capacity
            if fuel_cost <= tank_capacity:
                # Add the fuel cost to the minimum cost
                min_cost += fuel_cost
                
                # Update the fuel level
                fuel_level = tank_capacity - fuel_cost
            else:
                # Return "cancel road trip" if the fuel cost is greater than the tank capacity
                return "cancel road trip"
        else:
            # Update the fuel level
            fuel_level = fuel_level - distance
    
    # Return the minimum cost
    return min_cost

