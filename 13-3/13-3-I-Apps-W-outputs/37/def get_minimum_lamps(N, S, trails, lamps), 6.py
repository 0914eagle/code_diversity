
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
            queue.extend(graph[node] - visited)
    
    # Calculate the total distance of the minimum spanning tree
    total_distance = sum(d for _, d in tree)
    
    # Calculate the number of additional lamps needed
    needed_lamps = 0
    for node, distance in tree:
        if distance + S > total_distance:
            needed_lamps += 1
    
    # Return the number of additional lamps needed
    return needed_lamps

