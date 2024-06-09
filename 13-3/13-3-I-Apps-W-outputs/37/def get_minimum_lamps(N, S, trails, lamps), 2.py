
def get_minimum_lamps(N, S, trails, lamps):
    # Initialize a graph with the given trails
    graph = {i: set() for i in range(1, N + 1)}
    for a, b, d in trails:
        graph[a].add((b, d))
        graph[b].add((a, d))
    
    # Find the minimum spanning tree of the graph
    tree = []
    visited = set()
    queue = [(1, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node not in visited:
            visited.add(node)
            tree.append((node, distance))
            for neighbor, d in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + d))
    
    # Find the minimum number of additional lamps needed
    needed_lamps = 0
    for node, distance in tree:
        if node not in lamps and distance < S:
            needed_lamps += 1
    
    return needed_lamps

