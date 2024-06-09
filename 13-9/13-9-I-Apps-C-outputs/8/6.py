
def solve(distances, costs, tank_capacity):
    # Sort the distances and costs in ascending order
    sorted_distances = sorted(distances)
    sorted_costs = sorted(costs, key=lambda x: x[1])
    
    # Initialize the variables
    current_distance = 0
    current_cost = 0
    total_cost = 0
    gas_left = tank_capacity
    
    # Loop through the distances and costs
    for i in range(len(sorted_distances)):
        distance = sorted_distances[i]
        cost = sorted_costs[i][1]
        
        # Calculate the amount of gas needed for the next distance
        gas_needed = (distance - current_distance) // cost
        
        # Check if the gas needed is more than the gas left in the tank
        if gas_needed > gas_left:
            return "cancel road trip"
        
        # Add the cost of the next distance to the total cost
        total_cost += cost * gas_needed
        
        # Update the current distance and cost
        current_distance = distance
        current_cost = cost
        
        # Update the gas left in the tank
        gas_left -= gas_needed
    
    # Return the total cost
    return total_cost

