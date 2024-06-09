
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    curr_capacity = 0
    # Initialize the current distance traveled as 0
    curr_distance = 0
    # Sort the distances and costs in ascending order
    sorted_distances = sorted(distances)
    sorted_costs = sorted(costs)
    # Iterate through the distances and costs
    for i in range(n):
        # Calculate the distance to the next gas station
        next_distance = sorted_distances[i] - curr_distance
        # Calculate the cost to travel to the next gas station
        next_cost = sorted_costs[i] * (next_distance // 1000)
        # Check if the next gas station is within reach
        if next_distance + curr_capacity <= g:
            # Fill up the gas tank to the maximum capacity
            curr_capacity = g
            # Update the current distance traveled
            curr_distance = sorted_distances[i]
            # Update the minimum cost to travel to the rightmost gas station
            min_cost = min(min_cost, next_cost)
        else:
            # Fill up the gas tank to the next gas station
            curr_capacity = next_distance + curr_capacity - g
            # Update the current distance traveled
            curr_distance = sorted_distances[i]
            # Update the minimum cost to travel to the rightmost gas station
            min_cost = min(min_cost, next_cost + curr_capacity * sorted_costs[i])
    # Check if the trip is possible
    if curr_distance == sorted_distances[-1]:
        return min_cost
    else:
        return "cancel road trip"

