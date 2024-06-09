
def solve(n, g, distances, costs):
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    # Initialize the current gas tank capacity as 0
    current_capacity = 0
    # Iterate through the gas stations from left to right
    for i in range(n):
        # Calculate the distance from the current gas station to the rightmost gas station
        distance = distances[i]
        # Calculate the cost to travel from the current gas station to the rightmost gas station
        cost = costs[i]
        # Check if the current gas tank capacity is enough to travel to the next gas station
        if current_capacity >= distance:
            # Subtract the distance from the current gas tank capacity
            current_capacity -= distance
        else:
            # Calculate the amount of fuel needed to travel from the current gas station to the rightmost gas station
            fuel_needed = distance - current_capacity
            # Check if the fuel needed is less than or equal to the gas tank capacity
            if fuel_needed <= g:
                # Add the fuel needed to the current gas tank capacity
                current_capacity += fuel_needed
            else:
                # The gas tank is not enough to travel from the current gas station to the rightmost gas station, so cancel the road trip
                return "cancel road trip"
        # Add the cost to travel from the current gas station to the rightmost gas station to the minimum cost
        min_cost += cost
    # Return the minimum cost to travel to the rightmost gas station
    return min_cost

