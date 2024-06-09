
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
    def has_cycle(start):
        visited[start] = True
        for neighbor in graph[start]:
            if not visited[neighbor]:
                if has_cycle(neighbor):
                    return True
            elif neighbor != start:
                return True
        visited[start] = False
        return False

    # Function to get the cost of decorating the graph
    def get_cost(start):
        visited[start] = True
        cost = 0
        for neighbor in graph[start]:
            if not visited[neighbor]:
                cost += get_cost(neighbor)
        visited[start] = False
        return cost

    # Check if a cycle exists in the graph
    if has_cycle(1):
        return -1

    # Get the cost of decorating the graph
    return get_cost(1)

