
def solve(n, x, y, c, k):
    # Calculate the total cost of building a power station in each city
    total_cost = [c[i-1] for i in range(1, n+1)]
    
    # Calculate the total cost of connecting each pair of cities
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                total_cost[i-1] += k[i-1] + k[j-1] * abs(x[i-1] - x[j-1]) + k[j-1] * abs(y[i-1] - y[j-1])
    
    # Find the minimum total cost
    min_cost = min(total_cost)
    
    # Find the cities with the minimum total cost
    min_cities = [i for i in range(1, n+1) if total_cost[i-1] == min_cost]
    
    # Find the connections to be made
    connections = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and total_cost[i-1] + total_cost[j-1] == 2*min_cost:
                connections.append((i, j))
    
    return min_cost, min_cities, connections

