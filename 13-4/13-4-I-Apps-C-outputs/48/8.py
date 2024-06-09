
def solve(n, m, neighbors, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in neighbors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Breadth-first search from Alice's starting station
    queue = [(s, 0)]
    visited = set()
    while queue:
        station, time = queue.pop(0)
        if station == t:
            return time
        for neighbor in graph[station]:
            if neighbor not in visited:
                queue.append((neighbor, time + 1))
                visited.add(neighbor)
    
    # Breadth-first search from Bob's starting station
    queue = [(t, 0)]
    visited = set()
    while queue:
        station, time = queue.pop(0)
        if station == s:
            return time
        for neighbor in graph[station]:
            if neighbor not in visited:
                queue.append((neighbor, time + 1))
                visited.add(neighbor)
    
    return "never meet"

