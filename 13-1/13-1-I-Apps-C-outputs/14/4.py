
def get_min_cost(n, m, roads):
    # Initialize the cost array with -1 for all areas
    cost = [-1] * (n + 1)
    cost[1] = 0

    # Loop through each road and update the cost for the adjacent areas
    for a, b in roads:
        if cost[a] != -1 and cost[b] != -1:
            # If the cost of both areas is already known, update the cost for the current area
            cost[a] = (cost[a] + cost[b]) % 3
            cost[b] = (cost[a] + cost[b]) % 3
        elif cost[a] != -1:
            # If the cost of one area is already known, update the cost for the other area
            cost[b] = (cost[a] + 1) % 3
        elif cost[b] != -1:
            cost[a] = (cost[b] + 1) % 3
        else:
            # If neither area has a cost, assign a cost of 0 to the current area
            cost[a] = 0
            cost[b] = 1

    # Check if it's possible to decorate the city with the given properties
    for i in range(1, n + 1):
        if cost[i] == -1:
            return -1

    # If it's possible to decorate the city, return the minimum cost
    return min(cost)

