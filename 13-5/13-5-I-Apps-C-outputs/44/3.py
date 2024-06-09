
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    curr_capacity = 0
    # Initialize the current distance from the origin as 0
    curr_distance = 0
    # Initialize the current cost as 0
    curr_cost = 0

    # Sort the gas stations by their distance from the origin in ascending order
    sorted_distances = sorted(distances)

    # Iterate through the gas stations
    for i in range(n):
        # Calculate the distance from the current gas station to the next gas station
        next_distance = sorted_distances[i + 1] - sorted_distances[i]
        # Calculate the cost to travel from the current gas station to the next gas station
        next_cost = costs[i] * next_distance
        # Calculate the total cost to travel from the current gas station to the rightmost gas station
        total_cost = curr_cost + next_cost
        # Calculate the total distance from the current gas station to the rightmost gas station
        total_distance = curr_distance + next_distance
        # If the total distance is less than or equal to the gas tank capacity, update the minimum cost and break the loop
        if total_distance <= g:
            min_cost = min(min_cost, total_cost)
            break
        # If the total distance is greater than the gas tank capacity, refuel the car and update the current gas tank capacity and distance
        else:
            curr_capacity = g - curr_distance
            curr_distance = sorted_distances[i + 1]
            curr_cost = costs[i] * curr_capacity

    # If the minimum cost is infinity, return "cancel road trip"
    if min_cost == float('inf'):
        return "cancel road trip"
    # Otherwise, return the minimum cost
    else:
        return min_cost

