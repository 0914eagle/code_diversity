
def solve(n, g, distances, costs):
    # Sort the distances and costs in ascending order
    sorted_distances = sorted(distances)
    sorted_costs = sorted(costs)
    
    # Initialize the minimum cost to travel to the rightmost gas station as infinity
    min_cost = float('inf')
    
    # Iterate over the distances and costs
    for i in range(n):
        # Calculate the total distance traveled so far
        total_distance = sum(sorted_distances[:i+1])
        
        # Calculate the total cost so far
        total_cost = sum(sorted_costs[:i+1])
        
        # If the total distance is less than or equal to the fuel tank capacity, update the minimum cost
        if total_distance <= g:
            min_cost = min(min_cost, total_cost)
    
    # If it is possible to complete the trip without running out of gas, return the minimum cost
    if min_cost < float('inf'):
        return min_cost
    # Otherwise, return "cancel road trip"
    else:
        return "cancel road trip"

