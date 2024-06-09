
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
    
    # Find the shortest path from the university campus to the end of the minimum spanning tree
    path = []
    distance = 0
    for node, d in tree:
        if node == N:
            path.append(node)
            distance += d
            break
        path.append(node)
        distance += d
    
    # Find the shortest path from the university campus to the start of the minimum spanning tree
    path2 = []
    distance2 = 0
    for node, d in reversed(tree):
        if node == 1:
            path2.append(node)
            distance2 += d
            break
        path2.append(node)
        distance2 += d
    
    # Find the intersection points between the two paths
    intersections = set(path).intersection(path2)
    
    # Count the number of additional lamps needed
    needed_lamps = 0
    for intersection in intersections:
        if intersection not in lamps:
            needed_lamps += 1
    
    return needed_lamps

