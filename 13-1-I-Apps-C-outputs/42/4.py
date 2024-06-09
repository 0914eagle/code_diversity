
def solve(n, m, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    # Initialize the costs of decorations for each area
    costs = [0] * (n + 1)

    # Initialize the visited array to keep track of visited areas
    visited = [False] * (n + 1)

    # Function to check if a cycle can be formed with the given costs
    def is_cycle_possible(costs):
        for i in range(1, n + 1):
            if not visited[i]:
                if not dfs(i, costs, visited):
                    return False
        return True

    # Function to perform depth-first search on the graph
    def dfs(node, costs, visited):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            if not dfs(neighbor, costs, visited):
                return False
        return True

    # Function to calculate the total cost of decorations for a cycle
    def calculate_cost(costs):
        total_cost = 0
        for i in range(1, n + 1):
            total_cost += costs[i]
        return total_cost

    # Function to check if the total cost of decorations is odd
    def is_cost_odd(costs):
        total_cost = calculate_cost(costs)
        return total_cost % 2 == 1

    # Function to check if the costs of decorations along two adjacent roads are valid
    def is_valid_costs(costs, a, b):
        return (costs[a] + costs[b]) % 3 != 1

    # Function to find the minimum cost of decorations
    def find_min_cost():
        min_cost = float("inf")
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and is_valid_costs(costs, i, j):
                    costs[i] = 1
                    costs[j] = 2
                    if is_cycle_possible(costs) and is_cost_odd(costs):
                        min_cost = min(min_cost, calculate_cost(costs))
        return min_cost

    # Return the minimum cost of decorations
    return find_min_cost()

