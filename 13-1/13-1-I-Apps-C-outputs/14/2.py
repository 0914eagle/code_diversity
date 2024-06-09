
def get_min_cost(n, m, roads):
    # Initialize the cost array with -1 for all areas
    cost = [-1] * (n + 1)
    cost[1] = 0

    # Loop through each road and update the cost for the adjacent areas
    for i in range(m):
        a, b = roads[i]
        if cost[a] != -1 and cost[b] == -1:
            cost[b] = cost[a] + 1
        elif cost[a] == -1 and cost[b] != -1:
            cost[a] = cost[b] + 1
        elif cost[a] != -1 and cost[b] != -1:
            if (cost[a] + cost[b]) % 3 != 1:
                cost[b] = cost[a] + 1
            else:
                cost[a] = cost[b] + 1

    # Check if it is possible to decorate the city with the given properties
    for i in range(1, n + 1):
        if cost[i] == -1:
            return -1

    # Return the minimum cost
    return max(cost)

