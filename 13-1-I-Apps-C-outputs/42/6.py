
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
            if visited[i]:
                total_cost += costs[i]
        return total_cost

    # Function to find the minimum cost of decorations for the city
    def find_min_cost():
        min_cost = float("inf")
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i, costs, visited)
                if is_cycle_possible(costs):
                    total_cost = calculate_cost(costs)
                    min_cost = min(min_cost, total_cost)
                for j in range(1, n + 1):
                    visited[j] = False
        return min_cost

    # Find the minimum cost of decorations for the city
    min_cost = find_min_cost()

    # If a cycle is not possible, return -1
    if min_cost == float("inf"):
        return -1

    # Otherwise, return the minimum cost
    return min_cost

