
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    current_capacity = 0
    # Initialize the current distance from the origin as 0
    current_distance = 0
    # Initialize the current cost as 0
    current_cost = 0

    # Sort the distances and costs in ascending order
    sorted_distances = sorted(distances)
    sorted_costs = sorted(costs)

    # Iterate through the gas stations
    for i in range(n):
        # Calculate the distance from the current gas station to the next gas station
        distance_to_next = sorted_distances[i+1] - sorted_distances[i]
        # Calculate the cost to travel from the current gas station to the next gas station
        cost_to_next = sorted_costs[i] * distance_to_next
        # Calculate the total cost to travel from the origin to the current gas station
        total_cost = current_cost + cost_to_next
        # Calculate the total distance traveled from the origin to the current gas station
        total_distance = current_distance + distance_to_next
        # Check if the total distance traveled is less than or equal to the gas tank capacity
        if total_distance <= g:
            # Calculate the remaining gas tank capacity
            remaining_capacity = g - total_distance
            # Calculate the amount of gas needed to fill the gas tank
            gas_needed = remaining_capacity // distance_to_next
            # Calculate the total cost to fill the gas tank
            total_cost += gas_needed * sorted_costs[i]
            # Update the current gas tank capacity
            current_capacity = g
            # Update the current distance from the origin
            current_distance = total_distance
            # Update the current cost
            current_cost = total_cost
        else:
            # Calculate the amount of gas needed to fill the gas tank
            gas_needed = g // distance_to_next
            # Calculate the total cost to fill the gas tank
            total_cost += gas_needed * sorted_costs[i]
            # Update the current gas tank capacity
            current_capacity = g
            # Update the current distance from the origin
            current_distance = g
            # Update the current cost
            current_cost = total_cost
            # Break out of the loop
            break

    # Check if the total distance traveled is less than or equal to the gas tank capacity
    if current_distance <= g:
        # Return the minimum cost to travel to the rightmost gas station
        return current_cost
    else:
        # Return "cancel road trip"
        return "cancel road trip"

