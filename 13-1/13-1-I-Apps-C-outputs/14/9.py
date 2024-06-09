
def get_min_cost(n, m, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    # Initialize the cost of each area to 0
    costs = [0] * (n + 1)

    # Initialize the visited array to keep track of visited areas
    visited = [False] * (n + 1)

    # Function to check if a cycle exists in the graph
    def has_cycle(area):
        if visited[area]:
            return True
        visited[area] = True
        for neighbor in graph[area]:
            if has_cycle(neighbor):
                return True
        visited[area] = False
        return False

    # Function to get the cost of decorating the graph
    def get_cost(area):
        if costs[area] != 0:
            return costs[area]
        costs[area] = 1
        for neighbor in graph[area]:
            costs[area] += get_cost(neighbor)
        return costs[area]

    # Function to check if the cost of decorating the graph is odd
    def is_odd_cost():
        total_cost = 0
        for cost in costs:
            total_cost += cost
        return total_cost % 2 == 1

    # Function to check if the cost of decorating the graph is valid
    def is_valid_cost():
        for i in range(1, n + 1):
            for j in graph[i]:
                if (costs[i] + costs[j]) % 3 == 1:
                    return False
        return True

    # Function to get the minimum cost of decorating the graph
    def get_min_cost():
        min_cost = float("inf")
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                for j in graph[i]:
                    if not visited[j]:
                        visited[j] = True
                        min_cost = min(min_cost, get_cost(j))
                        visited[j] = False
                visited[i] = False
        return min_cost

    # Main function to solve the problem
    if has_cycle(1):
        return -1
    while not is_valid_cost():
        for i in range(1, n + 1):
            if costs[i] == 0:
                costs[i] = 1
        if not is_odd_cost():
            return -1
    return get_min_cost()

