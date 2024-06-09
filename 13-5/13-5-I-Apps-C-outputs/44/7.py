
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    current_capacity = 0
    # Initialize the current distance from the origin as 0
    current_distance = 0
    # Initialize the current cost as 0
    current_cost = 0

    # Sort the gas stations by their distances from the origin in ascending order
    sorted_distances = sorted(distances)

    # Iterate through the gas stations
    for i in range(n):
        # Calculate the distance from the current gas station to the next gas station
        distance_to_next = sorted_distances[i + 1] - sorted_distances[i]
        # Calculate the cost to travel from the current gas station to the next gas station
        cost_to_next = costs[i] * distance_to_next
        # Calculate the total cost to travel from the current gas station to the rightmost gas station
        total_cost = current_cost + cost_to_next
        # Calculate the total distance from the current gas station to the rightmost gas station
        total_distance = current_distance + distance_to_next
        # If the total distance is less than or equal to the gas tank capacity, update the minimum cost and move to the next gas station
        if total_distance <= g:
            min_cost = min(min_cost, total_cost)
            current_capacity -= distance_to_next
            current_distance = total_distance
            current_cost = total_cost
        # If the total distance is greater than the gas tank capacity, refuel the car and move to the next gas station
        else:
            # Calculate the amount of gas needed to reach the next gas station
            gas_needed = g - current_distance
            # Calculate the cost of the gas needed
            gas_cost = costs[i] * gas_needed
            # Update the minimum cost and move to the next gas station
            min_cost = min(min_cost, current_cost + gas_cost)
            current_capacity = g - gas_needed
            current_distance = sorted_distances[i + 1]
            current_cost = current_cost + gas_cost

    # If the minimum cost is infinity, it is not possible to complete the trip without running out of gas, so return "cancel road trip"
    if min_cost == float('inf'):
        return "cancel road trip"
    # Otherwise, return the minimum cost
    else:
        return min_cost

