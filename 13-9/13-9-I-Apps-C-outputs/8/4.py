
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as zero
    curr_capacity = 0
    # Iterate through the gas stations from left to right
    for i in range(n):
        # Calculate the distance from the current gas station to the rightmost gas station
        dist = distances[i] - distances[n-1]
        # Calculate the cost to travel from the current gas station to the rightmost gas station
        cost = costs[i] * dist
        # If the current gas tank capacity plus the distance to the rightmost gas station is less than or equal to the car's fuel tank capacity, update the minimum cost and current gas tank capacity
        if curr_capacity + dist <= g:
            min_cost = min(min_cost, cost)
            curr_capacity += dist
        # If the current gas tank capacity is greater than the car's fuel tank capacity, cancel the road trip
        elif curr_capacity > g:
            return "cancel road trip"
    # Return the minimum cost to travel to the rightmost gas station
    return min_cost

