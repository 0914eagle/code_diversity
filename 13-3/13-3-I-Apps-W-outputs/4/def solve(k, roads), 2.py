
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))

    # Find the minimum sum by performing a depth-first search and keeping track of the minimum time spent
    min_time = float("inf")
    for i in range(1, 2*k+1):
        visited = set()
        queue = [(i, 0)]
        while queue:
            node, time = queue.pop(0)
            if node not in visited:
                visited.add(node)
                min_time = min(min_time, time)
                for neighbor, t in graph[node]:
                    queue.append((neighbor, time + t))

    # Find the maximum sum by performing a breadth-first search and keeping track of the maximum time spent
    max_time = 0
    for i in range(1, 2*k+1):
        visited = set()
        queue = [(i, 0)]
        while queue:
            node, time = queue.pop(0)
            if node not in visited:
                visited.add(node)
                max_time = max(max_time, time)
                for neighbor, t in graph[node]:
                    queue.append((neighbor, time + t))

    return min_time, max_time

