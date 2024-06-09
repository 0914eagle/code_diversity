
def solve(n, x, y, c, k):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    # Initialize the optimal solution
    optimal_solution = []

    # Loop through all possible combinations of power stations and connections
    for power_stations in range(n + 1):
        for connections in itertools.combinations(range(n), power_stations):
            # Calculate the cost of the current combination
            cost = 0
            for i in range(n):
                if i in connections:
                    # Calculate the cost of connecting City i to its neighbors
                    cost += k[i] * len(connections)
                else:
                    # Calculate the cost of building a power station in City i
                    cost += c[i]

            # If the current combination has a lower cost than the minimum cost, update the minimum cost and the optimal solution
            if cost < min_cost:
                min_cost = cost
                optimal_solution = [power_stations, connections]

    # Return the optimal solution
    return optimal_solution

