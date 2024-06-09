
def solve(n, m, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    # Initialize the cost of decorating each area to 0
    costs = [0] * (n + 1)

    # Initialize the visited array to keep track of visited areas
    visited = [False] * (n + 1)

    # Function to decorate the city recursively
    def decorate(area, cost):
        # If the area is already visited, return
        if visited[area]:
            return

        # Mark the area as visited
        visited[area] = True

        # Add the cost of decorating the current area to the total cost
        costs[area] += cost

        # Recursively decorate the adjacent areas
        for adjacent in graph[area]:
            decorate(adjacent, cost)

    # Decorate the city starting from area 1
    decorate(1, 0)

    # Check if the cost of decorating each area is odd
    for i in range(1, n + 1):
        if costs[i] % 2 == 0:
            return -1

    # Return the total cost of decorating the city
    return sum(costs)

